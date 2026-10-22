class Employee:
    def work(self):
        print("Employee performs work")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Designer(Employee):
    def work(self):
        print("Designer creates designs")


employees = [Developer(), Designer(), Employee()]

for employee in employees:
    employee.work()