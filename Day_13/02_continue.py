# Continue skips the iteration but the loop contineues

for i in range(1,6):
    if i == 3:
        continue
    print(i)        # 1 2 4 5 


# Continue with while loop

i = 1
while(i <= 10):
    if(i == 5):
        i += 1
        continue
    print(i)        # 1 2 3 4 6 7 8 9 10
    i = i + 1

# Print numbers from 1 to 20 but skip even numbers.

for i in range(1,21):
    if(i % 2 == 0):
        continue
    print(i)