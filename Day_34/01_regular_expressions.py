# Regular Expressions -- A regular expression is a pattern used to find specific text inside a string

import re

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Pattern found!")
else:
    print("Pattern not found.")


text = "Python is easy. Python is powerful."

print(re.findall("Python", text))
print(re.sub("Python", "Java", text))


text = "My BCA roll number is 2026."

numbers = re.findall(r"\d+", text)

print(numbers)