import requests
from bs4 import BeautifulSoup
import pandas as pd
from mysql.connector import connect,Error
import mysql.connector
from sqlalchemy import create_engine

# try:
#     with connect(
#         host="localhost",
#         user="root",
#         password="SQLtest6384",
#     ) as connection:
#         create_db_query = "CREATE DATABASE Cars"
#         with connection.cursor() as cursor:
#             cursor.execute(create_db_query)
# except Error as e:
#     print(e)

conn=mysql.connector.connect(host="localhost", username="root",
                             password="SQLtest6384",database="Cars")


cursor=conn.cursor()
# sql ="""CREATE TABLE USEDCARS( Price VARCHAR(10), Mileage VARCHAR(10))"""
# cursor.execute(sql)

URL = "https://www.truecar.com/used-cars-for-sale/listings/bmw/z4/body-convertible/?sort[]=best_deal_desc_script"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("ul",class_="row mb-3 mt-1")
res_elements = results.find_all("li",class_="mt-3 flex grow col-md-6 col-xl-4")

price,mileage=[],[]

#Reduce elements' length to 20
for res_element in res_elements[:20]:
    price.append(res_element.find("span", {"data-test":"vehicleListingPriceAmount"}).get_text())
    mileage.append(res_element.find("div", {"data-test":"vehicleMileage"}).get_text())
    # print(price)
    # print(mileage)
    # print()

# print(price)
# print(mileage)

df = pd.DataFrame({'Price':price,'Mileage':mileage})
#       Price        Mileage
# 0   $18,994   81,185 miles
# 1    $8,350  105,789 miles
# 2   $10,500   29,567 miles
# 3    $7,500  119,724 miles
# ...

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host="localhost", db="Cars", user="root", pw="SQLtest6384"))

df.to_sql('USEDCARS', engine, index=False)

conn.commit()
conn.close()    