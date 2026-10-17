# Modules and Packages in Python

# 1. Math module
import math

print("Square root:", math.sqrt(64))
print("Factorial:", math.factorial(5))
print("Pi:", math.pi)

# 2. Import a specific function
from math import pow

print("Power:", pow(2, 3))

# 3. Module alias
import random as r

print("Random number:", r.randint(1, 10))

# 4. Date and time module
from datetime import date

print("Today's date:", date.today())

# 5. Current working directory
import os

print("Working directory:", os.getcwd())