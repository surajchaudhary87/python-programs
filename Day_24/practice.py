# File Handling in Python

# 1. Write content to a file
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python!\n")
    file.write("Learning file handling.\n")

print("File written successfully.")


# 2. Read the file
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("\nFile content:")
    print(content)


# 3. Append content to the file
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("This is Day 24.\n")

print("Content appended successfully.")


# 4. Read the file line by line
print("\nReading line by line:")

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# 5. Handle a missing file
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found!")
