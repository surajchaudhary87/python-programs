
import sqlite3

DATABASE = "day38.db"


def connect_database():
    return sqlite3.connect(DATABASE)


def setup_database():
    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                course TEXT NOT NULL,
                marks INTEGER NOT NULL
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM students")
        total = cursor.fetchone()[0]

        if total == 0:
            students = [
                ("Aman", "Python", 85),
                ("Rahul", "Java", 92),
                ("Priya", "Python", 78),
                ("Neha", "Java", 88),
                ("Rohit", "HTML", 65),
                ("Anjali", "Python", 95),
                ("Vikas", "HTML", 72),
                ("Pooja", "Java", 81)
            ]

            cursor.executemany("""
                INSERT INTO students (name, course, marks)
                VALUES (?, ?, ?)
            """, students)


def display_students():
    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students ORDER BY id")
        records = cursor.fetchall()

        print("\n--- All Students ---")
        for student in records:
            print(student)


def filter_students():
    marks = 80

    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name, course, marks
            FROM students
            WHERE marks > ?
        """, (marks,))

        print("\n--- Students Scoring Above 80 ---")
        for student in cursor.fetchall():
            print(student)


def sort_students():
    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name, marks
            FROM students
            ORDER BY marks DESC
        """)

        print("\n--- Students Sorted by Marks ---")
        for student in cursor.fetchall():
            print(student)


def show_top_students():
    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name, marks
            FROM students
            ORDER BY marks DESC
            LIMIT 3
        """)

        print("\n--- Top 3 Students ---")
        for student in cursor.fetchall():
            print(student)


def show_statistics():
    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                COUNT(*),
                SUM(marks),
                ROUND(AVG(marks), 2),
                MAX(marks),
                MIN(marks)
            FROM students
        """)

        result = cursor.fetchone()

        print("\n--- Student Statistics ---")
        print("Total Students:", result[0])
        print("Total Marks:", result[1])
        print("Average Marks:", result[2])
        print("Highest Marks:", result[3])
        print("Lowest Marks:", result[4])


def course_statistics():
    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT course, COUNT(*), ROUND(AVG(marks), 2)
            FROM students
            GROUP BY course
        """)

        print("\n--- Course Statistics ---")
        for course in cursor.fetchall():
            print(
                "Course:", course[0],
                "| Students:", course[1],
                "| Average:", course[2]
            )


def high_average_courses():
    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT course, AVG(marks)
            FROM students
            GROUP BY course
            HAVING AVG(marks) > ?
        """, (80,))

        print("\n--- Courses with Average Above 80 ---")
        for course in cursor.fetchall():
            print(course)


def main():
    setup_database()

    while True:
        print("\n===== ADVANCED SQLITE PROJECT =====")
        print("1. Display All Students")
        print("2. Filter Students")
        print("3. Sort Students")
        print("4. Show Top 3 Students")
        print("5. Show Statistics")
        print("6. Course Statistics")
        print("7. Courses with Average Above 80")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_students()
        elif choice == "2":
            filter_students()
        elif choice == "3":
            sort_students()
        elif choice == "4":
            show_top_students()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            course_statistics()
        elif choice == "7":
            high_average_courses()
        elif choice == "8":
            print("Thank you for using the project!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
