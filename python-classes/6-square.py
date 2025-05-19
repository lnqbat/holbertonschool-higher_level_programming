#!/usr/bin/python3
"""
Defines an empty class Square.
"""


class Square:
    """
    A Square class.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        A square init size.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        That a position of a square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the positions square.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value == 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        That square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        That print square #.
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
