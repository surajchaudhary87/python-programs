# File Handling -- Working with files 

# Opening a file -- open()
file = open("data.txt","r")
file.close()


#File opening modes

# 1. "r" -- Read an existing file
# 2. "w" -- Write to file; replaces existing content or creates the file
# 3. "a" -- Append content to the end a file or create it
# 4. "x" -- Create a new file; raises an error if it already exists
# 5. "rb" -- Read a file in binary mode


#Reading a file 
with open("data.txt","r") as  file:     #with automaticly close the file
    content = file.read()
    print()



# Writing a file
with open("data.txt","w") as file:
    file.write("Pyrhon file handling\n")
    file.write("This is Day 24.")



#Appending Data to a file
with open("data.txt","a") as file:
    file.write("\nI am practicing Python.")



#Reading a file line by line

with open("data.txt","r") as file:
    for line in file:
        print(line.strip())



#Using try and except

try:
    with open("data.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
    