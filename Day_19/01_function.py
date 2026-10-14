# Functions in Python

# 1. Basic function
def greet():                #Use def keyword for creating a function
    print("Hello, welcome to Python!")

greet()     #Function calling


# 2. Function with a prameter 
def greet_user(name):       #Function defination
    print("Hello",name)

greet_user("Suraj")
greet_user("Ram")



# 3. Function with two parameters
def add(a,b):
    print("Sum :",(a+b))

add(10,20)



# 4. Function to calculate a square
def square(num):
    print("Square :",(num*num))

square(5)



# 5. Function with return value
def multiply(a, b):
    return a * b

multiply(2,5)



# 6. Function with a default parameter
def welcome(name="Student"):
    print("Welcome",name)

welcome()
welcome("Suraj")



# 7. Check wether a number is even or odd
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print(even_odd(10))
print(even_odd(15))
print(even_odd(11))