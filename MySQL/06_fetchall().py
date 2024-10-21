import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

mydbc=conn.cursor()

#query="SELECT * FROM test")

mydbc.execute("SELECT * FROM test")

myresult=mydbc.fetchall()

print(myresult)

