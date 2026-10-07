# break -- Stopes the loop completele

for i in range(1,21):
    if i == 5:
        break
    print(i)        # 1 2 3 4 


# break with while loop

i = 1
while i <= 10:
    if i == 6:
        break
    print(i)           # 1 2 3 4 5
    i += 1



# Print numbers from 1 to 20, but stop when the number reaches 15.

for i in range(1,21):
    if i == 15:
        break
    print(i)