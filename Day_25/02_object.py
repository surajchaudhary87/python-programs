# Object -- An object is an instance of a class.

class Student:
    name = "Suraj"
    age = 19
    marks = 548

student1 = Student()        # Here 'student1' is object
print(student1.name)
print(student1.age)
print(student1.marks)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Suraj", 20)
student2 = Student("Aman", 19)

print(student1.name)
print(student2.name)