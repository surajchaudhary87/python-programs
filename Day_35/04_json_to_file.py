import json

student = {
    "name": "Suraj",
    "age": 20,
    "course": "BCA"
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("Data saved successfully!")