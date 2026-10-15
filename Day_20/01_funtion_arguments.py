# Function Arguments and Return Values

# 1. Positional arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Suraj", 20)


# 2. Keyword arguments
def show_details(name, course):
    print("Name:", name)
    print("Course:", course)


show_details(course="BCA", name="Suraj")


# 3. Default arguments
def greet(name="Student"):
    print("Hello", name)


greet()
greet("Suraj")


# 4. Return multiple values
def calculate(a, b):
    return a + b, a - b


sum_result, difference = calculate(10, 5)

print("Sum:", sum_result)
print("Difference:", difference)


# 5. Calculate percentage
def calculate_percentage(hindi, english, maths):
    total = hindi + english + maths
    return total / 300 * 100


percentage = calculate_percentage(80, 75, 90)

print(f"Percentage: {percentage:.2f}%")