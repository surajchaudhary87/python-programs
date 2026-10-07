# Create a password program using while and break

correct_password = "1234"

while True:
    password = input("Enter password: ")
    
    if(password == correct_password):
        print("Login successful")
        break
