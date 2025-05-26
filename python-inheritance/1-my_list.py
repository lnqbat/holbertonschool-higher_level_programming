#!/usr/bin/python3
"""
Defines a class MyList
"""


class MyList(list):
    """
    Class inherits from list:
    """

    def print_sorted(self):
        """
        Prints the list, but sorted
        """
        copy = self.copy()
        copy.sort()
        print(copy)
