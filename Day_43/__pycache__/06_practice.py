
import csv
import os

FILE_NAME = "students.csv"

FIELDS = ["id", "name", "course", "marks"]


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)

        print("CSV file created successfully!")


def add_student():
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ").strip()
        course = input("Enter course: ").strip()
        marks = float(input("Enter marks: "))

        if not name or not course:
            print("Name and course cannot be empty!")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100!")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                student_id,
                name,
                course,
                marks
            ])

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric values!")


def view_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n--- STUDENT RECORDS ---")

        found = False

        for row in reader:
            print(row)
            found = True

        if not found:
            print("No student records found.")


def search_student():
    search_id = input("Enter student ID to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["id"] == search_id:
                print("\nStudent Found:")
                print(row)
                return

    print("Student not found!")


def calculate_average():
    total = 0
    count = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["marks"])
            count += 1

    if count == 0:
        print("No records available.")
    else:
        average = total / count
        print("Average Marks:", round(average, 2))


def main():
    create_file()

    while True:
        print("\n===== STUDENT CSV MANAGER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Average Marks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            calculate_average()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
