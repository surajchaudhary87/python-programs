# append() -- Add one element at the end 

fruits = ["Apple","Mango"]

fruits.append("Banana")
print(fruits)           # Apple, Mango, Banana


# insert() -- Add an item at a specific index
fruits.insert(1,"Grapes")
print(fruits)           #Apple, Grapes, Mango, Banana


# remove() -- Remove an items by value
fruits.remove("Mango")
print(fruits)           #Apple, Grapes, Banana


# pop() -- Remove an items by index
fruits.pop(1)
print(fruits)           #Apple, Banana


numbers = [10,20,40,5,10,30,20]

# sort() -- Short the list in assending order
numbers.sort()


# max() -- Gives largest elements in list
# min() -- Gives smalest elements in list
print(max(numbers))     #40
print(min(numbers))     #5


# sum() -- Gives sum of all elements of list
print(sum(numbers))     #135