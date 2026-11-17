import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)