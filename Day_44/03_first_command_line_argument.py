import argparse

parser = argparse.ArgumentParser(
    description="Student Information Program"
)

parser.add_argument("name", help="Enter student name")
parser.add_argument("age", type=int, help="Enter student age")

args = parser.parse_args()

print("Student Name:", args.name)
print("Student Age:", args.age)