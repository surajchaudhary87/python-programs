import csv

students = [
    ["id", "name", "course", "marks"],
    [1, "Rahul", "Python", 85],
    [2, "Aman", "Java", 90],
    [3, "Neha", "HTML", 78]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully!")