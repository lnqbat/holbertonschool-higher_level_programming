#!/usr/bin/python3
"""
Print a rectangle
"""


class Rectangle:
    """
    That defines a rectangle:
    """
    def __init__(self, width=0, height=0):
        """
        Init width.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        To retrieve it.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        To set it.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        To retrieve it.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        To set it.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        That returns the rectangle area.
        """
        return self.height * self.width

    def perimeter(self):
        """
        That returns the rectangle perimeter.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
