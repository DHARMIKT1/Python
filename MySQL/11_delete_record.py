import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

mydbc=conn.cursor()

id=input("Enter Id :")

mydbc.execute("DELETE FROM test WHERE id="+id)

myresult=mydbc.fetchall()

conn.commit()

print("Record delete successfully!")

mydbc.close()
conn.close()

