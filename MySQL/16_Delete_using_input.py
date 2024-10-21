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

    student_id = int(input("Enter the student id of the record you want to delete : "))

    query = "DELETE FROM student WHERE student_id = %s"

    cursor.execute(query,(student_id,))

    conn.commit()

    if cursor.rowcount > 0:
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"No record found with Student ID {student_id}.")

except Error as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
