import json

json_data = '{"name": "Suraj", "age": 20, "course": "BCA"}'

student = json.loads(json_data)

print(student)
print(student["name"])
print(type(student))