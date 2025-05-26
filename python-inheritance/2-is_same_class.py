#!/usr/bin/python3
"""
That checks if an object is exactly.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance.
    """
    obj_type = type(obj)
    return obj_type is a_class
