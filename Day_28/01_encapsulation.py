# Encapsulation -- Encapsulation means combining data and the methods that work with that data inside a class, while controlling how the data is accessed or modified.

class Student:
    def __init__(self):
        self.name = "Suraj"

student = Student()
print(student.name)



class Student:
    def __init__(self):
        self._marks = 85

student = Student()
print(student._marks)  # Accessible, but intended for internal use



class Account:
    def __init__(self):
        self.__balance = 5000

account = Account()
# print(account.__balance)  # Raises AttributeError