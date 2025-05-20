#!/usr/bin/python3
"""
Print a rectangle
"""


class Rectangle:
    """
    That defines a rectangle:
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init width.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """
        Print STR.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            height = self.height
            width = self.width
            return '\n'.join(
                str(self.print_symbol) * width for _ in range(height))

    def __repr__(self):
        """
        Return a string representation.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Rectangle is deleted.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        That returns the biggest rectangle based on the area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        That returns a new Rectangle instance.
        """
        return cls(size, size)
