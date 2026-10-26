#Python Iterators and Iterables
#Project: Number Sequence Iterator

class NumberSequence:
    #Generate numbers from start to end, inclusive

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            number = self.current
            self.current += 1
            return number

        raise StopIteration


def main():
    # An iterable: a list
    numbers = [10, 20, 30]
    print("List items:")

    for number in numbers:
        print(number)

    # An iterator created from the list
    print("\nUsing an iterator:")
    number_iterator = iter(numbers)

    print(next(number_iterator))
    print(next(number_iterator))
    print(next(number_iterator))

    # A custom iterator
    print("\nCustom number sequence:")
    sequence = NumberSequence(1, 5)

    for number in sequence:
        print(number)


if __name__ == "__main__":
    main()
