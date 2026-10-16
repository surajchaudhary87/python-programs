# Lambda Functions in Python

# 1. Lambda with one parameter
square = lambda n: n * n
print("Square:", square(5))

# 2. Lambda with two parameters
add = lambda a, b: a + b
print("Sum:", add(10, 20))

# 3. Lambda with a condition
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print("Number:", check(7))

# 4. Using map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n * n, numbers))
print("Squares:", squares)

# 5. Using filter()
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 6. Sorting tuples by marks
students = [
    ("Rahul", 75),
    ("Aman", 90),
    ("Suraj", 82)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("Students by marks:", sorted_students)