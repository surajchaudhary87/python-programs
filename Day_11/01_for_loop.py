# Loop -- A loop repeats code for each items ina sequence or range.
# For loop 

for i in range(5): 
    print(i)         # 0 1 2 3 4 

# range() --- function
# range(5)  range(stop)


# range(start,stop)
for i in range(1,6):
    print(i)        # 1 2 3 4 5



#range(start,stop,step)
for i in range(2,11,2):
    print(i)        # 2,4,6,8,10


for i in range(5):
    print("Hello World!")       # Hello World!  Hello World!  Hello World!  Hello World!  Hello World!


# Print number 1 to 10
for i in range(1,11):
    print(i)


# Print even numbers 
for i in range(2,21,2):
    print(i)



# Print multiplication table 
num = int(input("Entere a number: "))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")