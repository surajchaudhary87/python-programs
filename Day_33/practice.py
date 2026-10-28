
"""
Decorators in Python
Topics:
1. Basic decorator
2. Decorators with arguments
3. Logging decorator
4. functools.wraps
"""

from functools import wraps


def simple_decorator(func):
    """Print messages before and after a function call."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result

    return wrapper


def log_function(func):
    """Display the name of the function being called."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@simple_decorator
def greet(name):
    """Greet a user."""
    print(f"Hello, {name}!")


@log_function
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    print("1. Basic Decorator")
    greet("Student")

    print("\n2. Decorator with Arguments")
    result = add(10, 20)
    print("Sum:", result)

    print("\n3. Preserved Function Metadata")
    print("Function name:", greet.__name__)
    print("Documentation:", greet.__doc__)


if __name__ == "__main__":
    main()
