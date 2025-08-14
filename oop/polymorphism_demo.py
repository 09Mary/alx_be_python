import math

class Shape:
    def area(self):
        """Base method that must be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
