# 1. Function for printing even and odd numbers from 1 to 50
def even_odd():
    print("Even numbers: ", end="")
    for i in range(1, 51):
        if i % 2 == 0:
            print(i, end=" ")

    print()
    print("Odd numbers: ", end="")
    for i in range(1, 51):
        if i % 2 == 0:
            continue
        else:
            print(i, end=" ")

    print()


even_odd()


# 2. Function for calculating the factorial of 5
def fact():
    factorial = 1
    for i in range(1, 6):
        factorial = factorial * i

    print("Factorial of 5:", factorial)


fact()


# 3. Function to create a list and print all elements using a for loop
def lst():
    list1 = [
        10, 20, 30, 40, 50,
        60, 70, 80, 90, 100,
        110, 120, 130, 140, 150
    ]

    for i in list1:
        print(i, end=" ")

    print()


lst()


# 4. Function to print the multiplication table of 2
def table():
    for i in range(1, 11):
        print(f"2 x {i} = {2 * i}")


table()


# 5. Function for greeting a user using a default parameter
def greet(name="Student"):
    print("Hello", name)


greet()
greet("Suraj")


# 6. Function for adding multiple parameters
def sum_digits(*num):
    total = 0

    for i in num:
        total += i

    print("Sum =", total)


sum_digits(10, 20, 30, 40, 50, 60, 70, 80, 90)
