#1.upper()
name = "Suraj"
print(name.upper())  #SURAJ


#2.lower()
name = "Suraj"
print(name.lower())  #suraj

#3.capitalize()
name = "suraj"
print(name.capitalize())  #Suraj


#4.title()
name = "suraj chaudhary"
print(name.title())  #Suraj Chaudhary


#5.strip()
name = "   Suraj   "
print(name.strip())  #Suraj --- Removes leading and trailing whitespace


#6.replace()
text = "I love programming"
print(text.replace("programming", "Python"))  #I love Python


#find()
text = "Hello, welcome to the world of programming"
print(text.find("welcome"))  #7 --- Returns the index of the first occurrence of the


#count()
text = "I love programming. Programming is fun."
print(text.count("programming"))  #2 --- Counts the occurrences of the substring


#startswith()
text = "Hello, welcome to the world of programming"
print(text.startswith("Hello"))  #True --- Checks if the string starts with the specified substring


#endswith()
text = "Hello, welcome to the world of programming"
print(text.endswith("programming"))  #True --- Checks if the string ends with the specified substring
