import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

mydbc=conn.cursor()

mydbc.execute("SELECT * FROM test WHERE id=188")

myresult=mydbc.fetchall()

print(myresult)

