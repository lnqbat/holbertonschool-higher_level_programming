#!/usr/bin/python3

"""
Text indentation
"""


def text_indentation(text):
    """
    Prints text with two newlines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
