# Nested if -- If statements inside if statements

age = 20
has_id = True

if age >= 18:           #IF first condition is true, then check the second condition
    if has_id:
        print("You are allowed to enter the club.") #Second condition is true, so this line will be executed
    else:
        print("You need an ID to enter the club.")


# Nested if with else statement


age = 20
has_id = False
if age >= 18:           #IF first condition is true, then check the second condition
    if has_id:
        print("You are allowed to enter the club.") 
    else:
        print("You need an ID to enter the club.")  #Second condition is false, so this line will be executed
else:
    print("You are not allowed to enter the club.") 



#Example of nested if with Marks

marks = 85
if marks >= 40:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")  #Second condition is true, so this line will be executed
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    elif marks >= 50:
        print("Grade: E")
else:
    print("Grade: F")
    