import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

mydbc=conn.cursor()

mydbc.execute("UPDATE test SET name='sanvi' WHERE id=2")

myresult=mydbc.fetchall()

conn.commit()

print("Record updated successfully!")

mydbc.close()
conn.close()

