import math


class Shape:
    """Base class for shapes."""

    def area(self):
        """Method meant to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override this method.")


class Rectangle(Shape):
    """Rectangle shape class."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape class."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle."""
        return math.pi * (self.radius ** 2)
