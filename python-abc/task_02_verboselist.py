#!/usr/bin/env python3

class VerboseList(list):
    """
    That extends the Python list class.
    """
    def append(self, item):
        """
        Adding the item to the list.
        """
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, iterable):
        """
        Extending the list.
        """
        print("Extended the list with [{}] items.".format(len(iterable)))
        super().extend(iterable)

    def remove(self, item):
        """
        Removing the item from the list.
        """
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)

    def pop(self, index=-1):
        """
        Popping the item from the list.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
