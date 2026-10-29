import re

phone = input("Enter a 10-digit phone number: ")

if re.fullmatch(r"\d{10}", phone):
    print("Format is valid.")
else:
    print("Invalid format.")