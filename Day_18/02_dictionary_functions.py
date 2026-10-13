#Dictionary functions 

student = {"name":"Suraj","course":"BCA","city":"Lucknow","marks":99,"age":19}

#pop() -- Remove a value 

student.pop("age")      #You can remove a element using there key
print(student)          #{'name':'Suraj', 'course':'BCA', 'city':'Lucknow', 'marks':99}


#keys() -- Returns all keys
print(student.keys())


#values() -- Returns all values
print(student.values())


#items() -- Returns key-value paires
print(student.items())


#get() -- Gets a value safely
print(student.get("name","Not Found"))


#update() -- Adds or updates value
#student.update()


#Loop through a Dictionary
for key,value in student.items():
    print(key,":",value)

