class Student:
    #Represents a student and their basic information.

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        #Display the student's information.
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def check_result(self):
        #Display whether the student passed or failed.
        if self.marks >= 33:
            print("Result: Pass")
        else:
            print("Result: Fail")


def main():
    # Create objects of the Student class
    student1 = Student("Suraj", 20, 85)
    student2 = Student("Aman", 19, 28)

    # Display information and results
    student1.display_details()
    student1.check_result()

    student2.display_details()
    student2.check_result()


if __name__ == "__main__":
    main()
