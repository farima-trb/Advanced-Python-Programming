import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_splits
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

session.get("https://www.truecar.com/used-cars-for-sale/listings/year-2010-2023/body-convertible/?page=1")

new_list=[]   
URL = "https://www.truecar.com/used-cars-for-sale/listings/year-2010-2023/body-convertible/?page=1"

for page in range(1,4):
    page = requests.get(URL.replace('=1',f'={page}'))
    soup = BeautifulSoup(page.content, "html.parser")

    def get_other_car_detail(href):
        car_detail_url = f"https://www.truecar.com{href}"
        car_detail_page = requests.get(car_detail_url)
        car_detail_soup = BeautifulSoup(car_detail_page.content, "html.parser")
        car_transmission = car_detail_soup.find('div',class_="row pt-3")
        children = car_transmission.findChildren("div" , recursive=False)
        return(((children[6]).find('div',class_="flex items-center").find('div',class_="flex items-center")).get_text())

    results = soup.find("ul",class_="row mb-3 mt-1")
    res_elements = results.find_all("li",class_="mt-3 flex grow col-md-6 col-xl-4")

    content,name, price, mileage, year, transmission=[],[],[],[],[],[]

    for res_element in res_elements:
        content.append(res_element.find("a",class_="linkable vehicle-card-overlay order-2").get("href"))
        name.append(res_element.find("span", class_="truncate").get_text())
        price.append(res_element.find("span", {"data-test":"vehicleListingPriceAmount"}).get_text())
        mileage.append(res_element.find("div", {"data-test":"vehicleMileage"}).get_text())
        year.append(res_element.find("span", class_="vehicle-card-year text-xs").get_text())


    for i in content:
        transmission.append(get_other_car_detail(i))
    
    for name, price, mileage, year,transmission in zip(name, price, mileage, year,transmission):
        new_list.append([name, price, mileage, year, transmission])   

   
df = pd.DataFrame(new_list, columns=['Name', 'Price', 'Mileage', 'Year', 'Transmission']) 
df.to_csv('raw_data.csv', index=False)

# Cleaning values in the lists
df2 = df.drop_duplicates(keep='first')

df2["Price"]=list(map(lambda p: int(p.replace('$','').replace(',','')), list(df2["Price"])))
df2["Mileage"]=list(map(lambda m: int(m.replace('miles','').replace(' ','').replace(',','')), list(df2["Mileage"])))

df2["Year"]= list(map(lambda y: int(y),list(df2["Year"])))
current_year=2023
df2["Year"]=list(map(lambda y: current_year-y,list(df2["Year"])))

df2["Transmission"]=list(map(lambda y: y.replace('FWD','Automatic Transmission').replace('RWD','Automatic Transmission'),list(df2["Transmission"])))
# Lable the categorical data 0 for Auto , 1 for Manual
df2["Transmission"]= LabelEncoder().fit_transform(df2["Transmission"])

df2.to_csv('cleaned_data.csv', index=False)

# Adding data to database table
conn=mysql.connector.connect(host="localhost", username="root",
                             password="SQLtest6384",database="Cars")

cursor=conn.cursor()

sql ="""CREATE TABLE CarInfo_test( Name VARCHAR(10), 'Price' VARCHAR(10),
        'Mileage' VARCHAR(10), 'Year' INT, 'Transmission' VARCHAR(25))"""
        
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host="localhost", db="Cars", user="root", pw="SQLtest6384"))

df2.to_sql('CarInfo', engine, index=False)

frame = pd.read_sql("select * from Cars.CarInfo", conn)
pd.set_option('display.expand_frame_repr', False)

conn.commit()
conn.close() 
    
    
# Prediction

# correlation check
corr = frame.corr()
# print(corr)

# positive correlation --> Mileage & Year
# negative correlation --> price & Mileage , Price & Year, Price & Transmission

frame = frame.drop(['Name'], axis=1)

# Create X and Y variables
# Mileage, Year, Transmission are X  &  Price is Y

X = frame.drop('Price', axis=1)
y = np.log(frame['Price'])

# Train and Test Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=42)

# Normalisation
norm = MinMaxScaler().fit(X_train)
X_train = norm.transform(X_train)
X_test = norm.transform(X_test)

# Implementing Linear Regression
model= LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
# print(f"predicted response:\n{y_pred}")

print(f"coefficient of determination: {model.score(X, y)}")
print(f"intercept: {model.intercept_}")
print(f"coefficients: {model.coef_}")
    
frame.insert(4, "Predicted Price", np.exp(y_pred), True)
print(frame)
