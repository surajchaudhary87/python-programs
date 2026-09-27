# Taking input from user with the help of input() function
# Syntax-- variable = input("Statement")

name = input("Enter your name: ")
print("Hello",name)

age = input("Enter your age: ")
print("Your age:",age)

# By default input() always returns a string(str)

print(type(age)) #Here you entered number but input function convert it into str

#Taking Integer input 
age = int(input("Enter your age: ")) #Here int() funtion typecast string into integer 
print(type(age)) #Output <class 'int'>

#Taking Float input

math_marks = float(input("Enter your math marks: "))
print("Your math marks:",math_marks)





