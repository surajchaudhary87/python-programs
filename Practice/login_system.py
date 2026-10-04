correct_username = "suraj"
correct_password = "1234"

user_name = input("Enter user name: ")
password = input("Enter your password: ")

if correct_username == user_name :
    if correct_password == password :
        print("Login successful")
    else :
        print("Wrong password")
else :
    print("Invalid username")