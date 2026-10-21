# Inheritance -- It allows one class to acquire attributes and methods from another class

class Animal:          #Pairentt class
    def eat(self):
        print("This animal eats food.")


class Dog(Animal):      #Child class
    def bark(self):
        print("This dog barks.")


dog1 = Dog()

dog1.eat()      #Inherited from Animal
dog1.bark()     #Defined in Dog