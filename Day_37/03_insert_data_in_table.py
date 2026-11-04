import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
    ("Rahul", "BCA", 85)
)

connection.commit()
connection.close()

print("Student added successfully!")