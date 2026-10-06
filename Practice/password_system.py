# Creating password system loop needs password until correct password is entered by the user

correct_password = "1234"
password = " "

while password != correct_password:
    password = input("Enter password: ")
    
    if(password == correct_password):
        print("Login successful")
        break
    else:
        print("Wrong password")
