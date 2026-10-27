# Generators -- A generator is a special type of iterator that produces values one at a time instead of creating and storing all values at once.

def count_numbers():
    yield 1
    yield 2
    yield 3


for number in count_numbers():
    print(number)


def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number


for number in even_numbers(10):
    print(number)


def colors():
    yield "Red"
    yield "Green"
    yield "Blue"


color_generator = colors()

print(next(color_generator))
print(next(color_generator))
print(next(color_generator))