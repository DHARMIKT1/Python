import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

mydbc=conn.cursor()

mydbc.execute("SELECT * FROM test WHERE id IN (188,101,103) ORDER BY id DESC")

myresult=mydbc.fetchall()

print(myresult)

