import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

cursor=conn.cursor()

query="INSERT INTO test (id,name,city,phone) VALUES (%s,%s,%s,%s)"

query_data=(188,"Dharmik Tank","Junagadh",123456789)

cursor.execute(query,query_data)

conn.commit()

print(f"Data '{query_data}' insert successfully.")

cursor.close()
conn.close()
