#!/usr/bin/env python3

class CountedIterator:
    """
    Define a class.
    """
    
    
    def __init__(self, iterable):
        """
        Init Counted Iterator.
        """
        self.iterator = iter(iterable)
        self.__count = 0
    def __next__(self):
        """
        Next method.
        """
        try:
            item = next(self.iterator)
            self.__count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Count
        """
        return self.__count
