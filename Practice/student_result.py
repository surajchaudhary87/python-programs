def student_result():

    name = input("Enter your name: ")

    hindi = int(input("Enter your Hindi marks: "))
    english = int(input("Enter your English marks: "))
    math = int(input("Enter your Maths marks: "))
    science = int(input("Enter your Science marks: "))
    social_science = int(input("Enter your Social Science marks: "))
    art = int(input("Enter your Art marks: "))

    # Check for invalid marks
    if (hindi < 0) or (english < 0) or (math < 0) or \
       (science < 0) or (social_science < 0) or (art < 0):

        print("Invalid marks")
        return

    # Check pass/fail
    if (hindi < 33) or (english < 33) or (math < 33) or \
       (science < 33) or (social_science < 33) or (art < 33):
        
        result = "Fail"
        
    else:
        result = "Pass"

    # Calculate total and percentage
    total = (hindi + english + math + science + social_science + art)
    percentage = total/ 6

    # Calculate grade
    if percentage >= 90:
        grade = "Excellent"
    elif percentage >= 60:
        grade = "Good"
    elif percentage >= 40:
        grade = "Pass"
    else:
        grade = "Fail"


    print("\nStudent:", name)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Result:", result)
    print("Grade:", grade)


student_result()