import json

student = {
    "name": "Suraj",
    "age": 20,
    "course": "BCA"
}

json_data = json.dumps(student)

print(json_data)
print(json.dumps(student, indent=4))
print(type(json_data))