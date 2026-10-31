import json

with open("student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student)
print("Name:", student["name"])
print("Course:", student["course"])