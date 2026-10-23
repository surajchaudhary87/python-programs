class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100.")


student = Student(85)

print(student.get_marks())

student.set_marks(92)
print(student.get_marks())

student.set_marks(150)