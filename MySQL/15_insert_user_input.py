import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_db"
        )

    cursor = conn.cursor()

    uname = input("Enter your username : ")
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    psw = input("Enter your password: ")

    query = "INSERT INTO users (uname, name, city, email, phone, psw) VALUES (%s, %s, %s, %s, %s, %s)"

    insert = (uname,name,city,email,phone,psw)

    cursor.execute(query,insert)
    conn.commit()

    print("user inserted successfully")

except Error as e:
        print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
        print("MySQL connection is closed")

#mydbc.close()
#conn.close()
