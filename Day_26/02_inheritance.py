class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display_course(self):
        print("Course:", self.course)


student1 = Student("Suraj", "BCA")

student1.display_name()
student1.display_course()