import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

cursor=conn.cursor()

query="INSERT INTO test (id,name,city,phone) VALUES (%s,%s,%s,%s)"

query_data= [(101,"Mihir","Shapur",251345),
             (102,"Uday","Rajkot",462356),
             (103,"Darshit","Bhuj",58213),
             (104,"Kunj","Junagadh",147856),
             (105,"Jenish","Jamanagar",14236589)
             ]

cursor.executemany(query,query_data)

conn.commit()

print("Multiple row insert successfully.")

cursor.close()
conn.close()
