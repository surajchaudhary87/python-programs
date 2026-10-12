# set{} -- A set of collection of unique elemenys. Set do not allow duplicates value

fruits = {"Apple", "Mango", "Banana"}
print(fruits)       #Apple Banana Mango

numbers = {10,20,30,10,20}
print(numbers)      #10,20,30   Here automaticly remove duplicate values

numbers.add(40)
print(numbers)      #10,20,30,40

even = {2,4,6,8,10}
odd = {1,3,5,7,9,}

print(even)     #2,4,6,8,10
print(odd)      #1,3,5,7,9

#If you want to create a Empty set then use set() function not {}, because empty curly braces create a dictionary

new_set = set()
print(type(new_set))
new_set.add(10)
new_set.add(20)
new_set.add(30)
new_set.add(40)

print(new_set)  #10,20,30,40