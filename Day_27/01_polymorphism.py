# Polymorphism -- Many forms

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


