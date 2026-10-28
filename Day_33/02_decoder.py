# Decorators with function arguments

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is starting")
        result = func(*args, **kwargs)
        print("Function is completed")
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


answer = add(10, 20)
print("Sum:", answer)


def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result

    return wrapper


@log_function
def calculate_square(number):
    return number * number


print("Result:", calculate_square(5))


from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running function...")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """Display a greeting."""
    print("Hello!")


greet()
print(greet.__name__)
print(greet.__doc__)