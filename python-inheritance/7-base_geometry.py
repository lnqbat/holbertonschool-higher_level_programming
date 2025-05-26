#!/usr/bin/python3
"""
Defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    Class for future geometry operations.
    """
    def area(self):
        """
        The area Raises an Exception to indicate that the method.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        That validates value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
