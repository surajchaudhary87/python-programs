# Iterator -- An iterator is an object that provides items one at a time.

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
# print(next(iterator))  # Raises StopIteration


word = "PYTHON"       # Iterable
letter_iterator = iter(word)  # Iterator

print(next(letter_iterator))  # P
print(next(letter_iterator))  # Y


numbers = [1, 2, 3]
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break



class CountToThree:
    def __init__(self):
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 3:
            result = self.number
            self.number += 1
            return result

        raise StopIteration


counter = CountToThree()

for number in counter:
    print(number)