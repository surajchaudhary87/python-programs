
import argparse


def calculate_result(name, marks):
    total = sum(marks)
    percentage = total / len(marks)

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 45:
        grade = "C"
    elif percentage >= 33:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    if any(mark < 33 for mark in marks):
        print("Result: FAIL")
    else:
        print("Result: PASS")


def main():
    parser = argparse.ArgumentParser(
        description="Student Marks Calculator"
    )

    parser.add_argument(
        "name",
        help="Student name"
    )

    parser.add_argument(
        "marks",
        nargs=5,
        type=int,
        help="Enter marks of five subjects"
    )

    args = parser.parse_args()

    if any(mark < 0 or mark > 100 for mark in args.marks):
        parser.error("Marks must be between 0 and 100.")

    calculate_result(args.name, args.marks)


if __name__ == "__main__":
    main()
