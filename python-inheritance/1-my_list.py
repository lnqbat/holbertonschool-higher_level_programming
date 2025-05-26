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
        Newlist = self.copy()
        for i in range(len(Newlist)):
            for j in range(i + 1, len(Newlist)):
                if Newlist[i] > Newlist[j]:
                    Newlist[i], Newlist[j] = Newlist[j], Newlist[i]
        print(Newlist)
