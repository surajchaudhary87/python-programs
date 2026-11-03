# SQLite Database in Python
# What is a database? -- A database is an organized collection of data that can be stored, accessed, managed, and updated

import sqlite3

connection = sqlite3.connect("students.db")

print("Database connected successfully!")

connection.close()