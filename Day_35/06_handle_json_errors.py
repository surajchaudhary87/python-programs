import json

json_data = '{"name": "Suraj", "age": 20'

try:
    student = json.loads(json_data)
    print(student)

except json.JSONDecodeError:
    print("Invalid JSON data!")