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

    query= """
        SELECT student.student_id, student.name, student_mark.subject, student_mark.score
        FROM student
        LEFT JOIN student_mark ON student.student_id = student_mark.student_id;
        """

    cursor.execute(query)

    results = cursor.fetchall()
    for row in  results:
                print(f"Student ID: {row[0]}, Name: {row[1]}, Subject: {row[2] if row [2] else 'No Subject'}, Score: {row[3] if row [3] else 'No Score'} ")

except  Error as e:
        print(f"Error : {e}")

finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
