# Type Casting-- Changing one datatype into other datadype.

age = "21"
print(type(age))  #<class 'str'>

age = int(age)    #str to int 
print(type(age))  #<class 'int'>

x = "10.5"
print(type(x))    #<class 'str'>

x = float(x)      #str to float
print(type(x))    #<class 'float'>

mark = 97
print(type(mark)) #<class 'int'>

mark = str(mark)  #str to int
print(type(mark)) #<class 'str'>

print(bool(1))    #True
print(bool(0))    #False

print(bool(""))   #False
print(bool("Python"))  #True
