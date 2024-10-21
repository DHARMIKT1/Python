import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )

cursor=conn.cursor()

query="CREATE DATABASE IF NOT EXISTS python_db"

cursor.execute(query)

conn.commit()

print("Database 'python_db' created successfully.")

cursor.close()
conn.close()
