#!/usr/bin/python3
"""
Defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    Class for future geometry operations.
    """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    That def Rectangle.
    """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square that inherits
    """
    def __init__(self, size):
        """
        Init square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Area a square.
        """
        return self.__size ** 2
