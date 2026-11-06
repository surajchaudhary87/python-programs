# Advanced SQLite Queries
# WHERE — Filter records -- WHERE selects records that match a condition

import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM students WHERE marks >= ?",
    (80,)
)

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()