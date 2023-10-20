import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import re

conn=mysql.connector.connect(host="localhost", username="root",
                             password="SQLtest6384",database="Learn")

cursor=conn.cursor()

sql ="""CREATE TABLE Information( username VARCHAR(60), password VARCHAR(20))"""

username_list,password_list=[],[]


# check input validity
regex = r'\b[A-Za-z0-9_]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'
 

# email address pattern:
# 2 string  
# 1 expression (string or both digit and string)
# seperated by @ and .
# expression@string.string
if __name__ == '__main__':
    
    print("\nEnter your email address:")
    username_temp=input()  
    
    if (re.fullmatch(regex, username_temp)!=None):
        pass
    
    else:
        while(re.fullmatch(regex, username_temp)==None):
            print("\nInvalid Email")
            print("\Follow Thiss Pattern: expression@string.string")
            print("\nEnter your email address again:")
            username_temp=input() 
            continue
        
    username_list.append(username_temp)


# password pattern:
# digit and string
print("\nEnter your password:")
password_temp=input()
password_list.append(password_temp)


df = pd.DataFrame({'username':username_list,'password':password_list})
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host="localhost", db="Learn", user="root", pw="SQLtest6384"))
df.to_sql('Information', engine, index=False)

conn.commit()
conn.close()