
"""
Python Abstraction
Project: Shape Area Calculator
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def display_name(self):
        """Display the shape's name."""
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display_name(self):
        print("Shape: Rectangle")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def display_name(self):
        print("Shape: Circle")


def display_shape(shape):
    """Display a shape's name and area."""
    shape.display_name()
    print(f"Area: {shape.area():.2f}")


def main():
    rectangle = Rectangle(10, 5)
    circle = Circle(7)

    display_shape(rectangle)
    print()

    display_shape(circle)


if __name__ == "__main__":
    main()
