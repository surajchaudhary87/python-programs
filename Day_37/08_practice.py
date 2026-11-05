
"""
SQLite Database in Python
Project: Student Database Management System

Features:
1. Add student
2. View all students
3. Search student by ID
4. Update student marks
5. Delete student
"""

import sqlite3


DATABASE = "students.db"


def connect_database():
    """Connect to the SQLite database and create the table."""
    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)

    return connection


def add_student():
    """Add a new student."""
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    try:
        marks = int(input("Enter marks: "))

        if not name or not course:
            print("Name and course cannot be empty.")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        with connect_database() as connection:
            connection.execute(
                """
                INSERT INTO students (name, course, marks)
                VALUES (?, ?, ?)
                """,
                (name, course, marks)
            )

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric marks.")
    except sqlite3.Error as error:
        print("Database error:", error)


def view_students():
    """Display all student records."""
    try:
        with connect_database() as connection:
            students = connection.execute(
                "SELECT * FROM students ORDER BY id"
            ).fetchall()

        if not students:
            print("No student records found.")
            return

        print("\n--- Student Records ---")

        for student in students:
            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Course: {student[2]} | "
                f"Marks: {student[3]}"
            )

    except sqlite3.Error as error:
        print("Database error:", error)


def search_student():
    """Search for a student using their ID."""
    try:
        student_id = int(input("Enter student ID: "))

        with connect_database() as connection:
            student = connection.execute(
                "SELECT * FROM students WHERE id = ?",
                (student_id,)
            ).fetchone()

        if student:
            print("\nStudent found:")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Course:", student[2])
            print("Marks:", student[3])
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")
    except sqlite3.Error as error:
        print("Database error:", error)


def update_student():
    """Update a student's marks."""
    try:
        student_id = int(input("Enter student ID: "))
        marks = int(input("Enter new marks: "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        with connect_database() as connection:
            cursor = connection.execute(
                "UPDATE students SET marks = ? WHERE id = ?",
                (marks, student_id)
            )

        if cursor.rowcount > 0:
            print("Student marks updated successfully!")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter valid numeric values.")
    except sqlite3.Error as error:
        print("Database error:", error)


def delete_student():
    """Delete a student using their ID."""
    try:
        student_id = int(input("Enter student ID: "))

        with connect_database() as connection:
            cursor = connection.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id,)
            )

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")
    except sqlite3.Error as error:
        print("Database error:", error)


def main():
    """Display the application menu."""
    while True:
        print("\n===== STUDENT DATABASE SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
