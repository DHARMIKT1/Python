import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
    )

cursor=conn.cursor()

query="""
            CREATE TABLE IF NOT EXISTS test(
            id int PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            phone VARCHAR(10) NOT NULL
            )
      """

cursor.execute(query)

conn.commit()

print("Table 'test' created successfully.")

cursor.close()
conn.close()
