# Python Inheritance
# Project: Employee Management System


class Employee:
    """Parent class containing common employee information."""

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


class Developer(Employee):
    """Child class for developers."""

    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def display_role(self):
        print("Role: Developer")
        print(f"Programming Language: {self.programming_language}")


class Designer(Employee):
    """Child class for designers."""

    def __init__(self, name, employee_id, design_tool):
        super().__init__(name, employee_id)
        self.design_tool = design_tool

    def display_role(self):
        print("Role: Designer")
        print(f"Design Tool: {self.design_tool}")


def main():
    developer = Developer("Suraj", 101, "Python")
    designer = Designer("Aman", 102, "Figma")

    print("--- Developer Details ---")
    developer.display_details()
    developer.display_role()

    print("\n--- Designer Details ---")
    designer.display_details()
    designer.display_role()


if __name__ == "__main__":
    main()
