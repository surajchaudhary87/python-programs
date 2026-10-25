
"""
OOP Revision
Project: Student Management System
"""

from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract parent class for people."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_role(self):
        """Display the person's role."""
        pass

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    """Student class inherits from Person."""

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.__marks = 0
        self.set_marks(marks)

    def set_marks(self, marks):
        """Accept marks only between 0 and 100."""
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100.")

    def get_marks(self):
        return self.__marks

    def display_role(self):
        print("Role: Student")

    def display_result(self):
        print(f"Marks: {self.__marks}")
        if self.__marks >= 33:
            print("Result: Pass")
        else:
            print("Result: Fail")


class Teacher(Person):
    """Teacher class also inherits from Person."""

    def display_role(self):
        print("Role: Teacher")


def show_person(person):
    """Polymorphism: works with different Person objects."""
    person.display_role()
    person.display_details()


def main():
    student = Student("Suraj", 20, 85)
    teacher = Teacher("Amit", 35)

    print("--- Student Details ---")
    show_person(student)
    student.display_result()

    print("\n--- Teacher Details ---")
    show_person(teacher)


if __name__ == "__main__":
    main()
