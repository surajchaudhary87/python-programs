import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (1,)
)

connection.commit()

print("Student deleted!")

connection.close()