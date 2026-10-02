# Conditional Statements

age = 20

# 1. if statement
if age >= 18:
    print("You are eligible to vote.")  #You are eligible to vote.


# 2. if-else statement
if age >= 18:
    print("You are eligible to vote.")  #You are eligible to vote.
else:
    print("You are not eligible to vote.")


# 3. if-elif-else statement
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")    # You are an adult.
else:
    print("You are a senior citizen.")
    