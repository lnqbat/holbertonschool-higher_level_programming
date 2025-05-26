#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    """
    If the object is an instance of a class that inherited
    """
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    return False
