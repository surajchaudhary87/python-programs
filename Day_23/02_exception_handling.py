# try and except

try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("You cannot division by zero!")
except ValueError:
    print("Plese enter a valid integer")


#Using else 

try:
    num = int(input("Enter a number: "))
    result = 100/num
except(ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
else:
    print("Result:",result)     #if not accure any exception then run else block



#Using finally -- finally block executes whether an exception occurs or not provide normal control flow reaches it
try:
    num = int(input("Enter a number: "))
    print(10/num)
except(ValueError,ZeroDivisionError):
    print("Enter a vailid number")
finally:
    print("Program finished")