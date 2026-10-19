#Practical Project -- Student Record Saver

name = input("Enter student name: ")
marks = input("Enter student marks: ")

with open("students.txt","a") as file:
    file.write(f"Name : {name}, Marks: {marks}\n")

print("Student record saved successfully!")