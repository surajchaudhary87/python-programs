import json

students = [
    {"id": 1, "name": "Rahul", "marks": 85},
    {"id": 2, "name": "Aman", "marks": 90},
    {"id": 3, "name": "Priya", "marks": 78}
]

# Save records
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

# Read records
with open("students.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Display records
for student in data:
    print(
        f"ID: {student['id']}, "
        f"Name: {student['name']}, "
        f"Marks: {student['marks']}"
    )