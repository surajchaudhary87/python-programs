#  For printing square
square = lambda n: n*n
print(square(5))        #25


# Lambda with 2 paramers
add  = lambda a,b: a + b
print(add(10,20))   #30
print(add(10,2))    #12


# Lambda with Conditions
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(2))     #Even
print(check(5))     #Odd


# Lambda with filter()
numbers = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda n: n % 2 == 0,numbers))

print(numbers)


# Lambda with sorted()
student = {
    {"Ranhul",75},
    {"Aman",90},
    {"Suraj",99}
}

result = sorted(student,key=lambda student: student[1])
print(result)
