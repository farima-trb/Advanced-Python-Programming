import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import pandas as pd
from mysql.connector import connect,Error
import mysql.connector

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

df2.to_csv('cleaned_data.csv', index=False)


