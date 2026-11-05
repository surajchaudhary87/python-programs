import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "UPDATE students SET marks = ? WHERE id = ?",
    (95, 1)
)

connection.commit()

print("Student marks updated!")

connection.close()