#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data structure.
"""


def class_to_json(obj):
    """
    Data structure (list, dictionary, string, integer and boolean) for JSON.
    """
    return obj.__dict__
