# Retrieve data from a database
# Use SELECT to read records

import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)
