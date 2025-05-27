"""
Shapes, Interfaces, and Duck Typing.
"""
from abc import ABC, abstractmethod
from math import pi



class Shape(ABC):
    """
    A class shape.
    """
    @abstractmethod
    def area(self):
        """
        The area of shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        The perimeter shape.
        """
        pass


class Circle(Shape):
    """
    A class Circle.
    """
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        """
        area circle.
        """
        return pi * self.__radius ** 2

    def perimeter(self):
        """
        A perimeter circle.
        """
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    That define a Rectangle.
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """
        Area Rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        That returns the rectangle perimeter.
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Prints the area and perimeter.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
