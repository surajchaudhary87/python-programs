# Decorator -- A decorator is a function that takes another function, adds some behavior to it, and returns a function

def welcome():
    print("Welcome to Python!")


def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


welcome = my_decorator(welcome)
welcome()


def my_decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished!")

    return wrapper


@my_decorator
def greet():
    print("Hello, student!")


greet()
