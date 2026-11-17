import csv

students = [
    {"id": 1, "name": "Rahul", "marks": 85},
    {"id": 2, "name": "Aman", "marks": 90}
]

with open("students.csv", "w", newline="") as file:

    fields = ["id", "name", "marks"]

    writer = csv.DictWriter(
        file,
        fieldnames=fields
    )

    writer.writeheader()
    writer.writerows(students)

print("Records saved!")