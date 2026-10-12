numbers = {10,20,30}

#add() -- Adding a value
numbers.add(40)
print(numbers)      #10,20,30,40


#remove() -- Remove a element 
numbers.remove(10)
print(numbers)      #20,30,40


#discard() -- Remove a element if present otherwise do nothing but does not show error
numbers.discard(50)
print(numbers)      #10,20,40
