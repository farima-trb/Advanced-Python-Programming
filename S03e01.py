import mysql.connector

conn=mysql.connector.connect(host="localhost", username="root",
                             password="SQLtest6384",database="Learn")

cursor=conn.cursor()

sql ="""CREATE TABLE EMPLOYEE( Name CHAR(20), Weight INT, Height INT)"""

row1 = """INSERT INTO EMPLOYEE(Name, Weight, Height)
                        VALUES ('Amin', 75, 180)"""
row2 = """INSERT INTO EMPLOYEE(Name, Weight, Height)
                        VALUES ('Mahdi', 90, 190)"""    
row3 = """INSERT INTO EMPLOYEE(Name, Weight, Height)
                        VALUES ('Mohammad', 75, 175)"""    
row4 = """INSERT INTO EMPLOYEE(Name, Weight, Height)
                        VALUES ('Ahmad', 60, 175)"""        

cursor.execute(row1)    
cursor.execute(row2)
cursor.execute(row3)
cursor.execute(row4)

# put the info in a list    
cursor.execute("SELECT * FROM EMPLOYEE")
rows = cursor.fetchall()
result_list = [list(row) for row in rows]
# print(result_list) 
# [['Amin', 75, 180], ['Mahdi', 90, 190], ['Mohammad', 75, 175], ['Ahmad', 60, 175]]

# sort the info
result_list.sort(key= lambda result_list:result_list[2])
result_list.reverse()

for i in range(1,len(result_list)):
	if result_list[i][2]==result_list[i-1][2]:
		if result_list[i-1][1]>result_list[i][1]:
			temp=result_list[i-1]
			result_list[i-1]=result_list[i]
			result_list[i]=temp

sorted_list=result_list

# print sorted info
for i in range(0,len(sorted_list)):
	print(sorted_list[i][0],sorted_list[i][1],sorted_list[i][2])

conn.commit()
conn.close()


