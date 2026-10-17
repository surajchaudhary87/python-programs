# Module -- A module is a Python file containing code, such as functions, variables, and classes, that can be reused in another Python file.

import maths    #Imports the moldule

print(maths.add(10,20))     #30  Call the add() funtion
print(maths.multiply(5,4))  #20  Call the multiply() function


#Diffrent ways to import a module

import math
print(math.sqrt(25))    #5.0
print(math.pi)          #3.14


# 2. Import a specific function
from math import sqrt
print(sqrt(36))         #6.0


# 3. Use an alias
import math as m
print(m.factorial(5))       #120


# Random number importing
import random
print(random.randint(1,10))


# Importing date and time
from datetime import date
print(date.today())


#Import os
import os
print(os.getcwd())

