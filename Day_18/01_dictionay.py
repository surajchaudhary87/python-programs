#Dictionary{} -- A dictionary stores data in key-value pairs 

student = {
    "name":"Suraj",
    "age":19,
    "course":"BCA"
}

print(student)      #{'name': 'Suraj', 'age': 20, 'course': 'BCA'}

print(student["name"])  #Suraj
print(student["course"])  #BCA


student2 = {
    "name": "Ram",
    "age": 20,
    "course": "BCA"
}

print(student2)     #{'name':'Ram', 'age':20, 'course':'BCA'}


print(student2["name"])     #Ram
print(student2["course"])     #BCA



#Add and Update values

student3 = {"name":"Suraj","age":20}

# Add a new key
student3["city"] = "Basti"

#Update an existing value
student3["age"] = 21

print(student3)        #{'name':'Suraj', 'age':21, 'city':'Basti'}


student3["marks"] = 98  #If key not present in dictionary then add it if already present key then overrite.