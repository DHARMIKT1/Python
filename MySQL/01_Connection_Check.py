import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    )

cursor = conn.cursor()

if conn.is_connected():
    print("Connected to MySQL database")
else:
    print("Connection Failed")

conn.close()
