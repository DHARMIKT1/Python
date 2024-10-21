import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

mydbc=conn.cursor()

query = """
        SELECT dt.id, dt.name, dt.city, dt.phone, 
               dm.m1, dm.m2, dm.m3 
        FROM test dt 
        LEFT JOIN mark dm 
        ON dt.id = dm.id
        """
mydbc.execute(query)

myresult=mydbc.fetchall()

print(myresult)

for row in myresult:
    print(row)

mydbc.close()
conn.close()

