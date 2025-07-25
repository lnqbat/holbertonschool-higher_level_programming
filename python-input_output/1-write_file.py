#!/usr/bin/python3
"""
That writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    That writes a string to a text file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
