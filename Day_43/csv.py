# 1. What is a CSV File?
#   --CSV stands for Comma-Separated Values.

#   --It stores data in rows, with values generally separated by commas.

# EXAMPLE:
'''id,name,course,marks
1,Rahul,Python,85
2,Aman,Java,90
3,Neha,HTML,78
4,Priya,Python,95'''

import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)