
"""
Generators in Python
Topics:
1. Basic generator
2. Generator with a loop
3. Using next()
4. Generator expression
5. Practical example: generating even numbers
"""


def count_numbers():
    """Generate numbers one at a time."""
    yield 1
    yield 2
    yield 3


def even_numbers(limit):
    """Generate even numbers from 2 up to the limit."""
    for number in range(2, limit + 1, 2):
        yield number


def countdown(start):
    """Generate a countdown from start to 1."""
    while start >= 1:
        yield start
        start -= 1


def main():
    print("1. Basic Generator")
    for number in count_numbers():
        print(number)

    print("\n2. Even Numbers")
    for number in even_numbers(10):
        print(number)

    print("\n3. Using next()")
    color_generator = (color for color in ["Red", "Green", "Blue"])
    print(next(color_generator))
    print(next(color_generator))
    print(next(color_generator))

    print("\n4. Countdown")
    for number in countdown(5):
        print(number)


if __name__ == "__main__":
    main()
