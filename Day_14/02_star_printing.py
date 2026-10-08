# Printing stars using nested loop

for i in range(1,4):
    for j in range(1,4):
        print("*",end="")
    print()


#Increasing Star Pattern
for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()


# Increasing Number Print

for i in range(1,6):
    for j in range(i):
        print(j, end="")
    print()


# Print a 5 x 5 multiplication tabel pattern.

for i in range(1,6):
    for j in range(1,6):
        print((i*j),end="")
    print()


# Number pairs from 1 to 3

for i in range(1,4):
    for j in range(1,4):
        print(i,j)