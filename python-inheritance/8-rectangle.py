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
    def __init__(self, width, height):
        """
        Init Rectangle width and height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
