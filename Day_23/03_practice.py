# Exception Handling in Python

# 1. Handle division by zero and invalid input
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program finished.")


# 2. Handle an invalid list index
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("List index does not exist.")


# 3. Handle a missing dictionary key
student = {"name": "Suraj", "course": "BCA"}

try:
    print(student["age"])

except KeyError:
    print("Student age was not found.")