#List-- A list is a collection of items stored in single variable

#Creation
fruits = ["Apple","Mango","Banan","Orange"]
numbers = [10,20,30,40,50]
decimalNumbers = [10.5,20.5,30.5,40.5]
mixed = ["Ram",10,"Seeta",10.5,True]


#Access list items  List indexing start at 0
print(fruits[0])    #Apple  
print(fruits[1])    #Mango
print(fruits[-1])   #Orange


#Changing a list items 
fruits[1] = "Grapes"
print(fruits[1])    #Grapes


#Adding items to a list
fruits.append("Apple")
print(fruits[-1])   #Apple