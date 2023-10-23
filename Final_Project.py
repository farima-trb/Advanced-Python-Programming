import requests
from bs4 import BeautifulSoup
import pandas as pd
from mysql.connector import connect,Error
import mysql.connector



new_list=[]   

for page in range(1,200):
    URL = "https://www.truecar.com/used-cars-for-sale/listings/year-2010-2023/body-convertible/"
    page = requests.get(URL)
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

    content,name, price, mileage, color, transmission=[],[],[],[],[],[]

    for res_element in res_elements:
        content.append(res_element.find("a",class_="linkable vehicle-card-overlay order-2").get("href"))
        name.append(res_element.find("span", class_="truncate").get_text())
        price.append(res_element.find("span", {"data-test":"vehicleListingPriceAmount"}).get_text())
        mileage.append(res_element.find("div", {"data-test":"vehicleMileage"}).get_text())
        color.append(res_element.find("div", {"data-test":"vehicleCardColors"}).get_text())


    for i in content:
        transmission.append(get_other_car_detail(i))

    
    for name, price, mileage, color,transmission in zip(name, price, mileage, color,transmission):
        new_list.append([name, price, mileage, color, transmission])   

   
df = pd.DataFrame(new_list, columns=['Name', 'Price', 'Mileage', 'Color', 'Transmission']) 
df.to_csv('raw_data.csv', index=False)


    

    
 