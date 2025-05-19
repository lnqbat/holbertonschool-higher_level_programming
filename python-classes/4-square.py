#!/usr/bin/python3
"""
Defines an empty class Square.
"""


class Square:
    """
    A Square class.
    """
    def __init__(self, size=0):
        """
        A square init size.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        That square area.
        """

        return self.__size ** 2
