#!/usr/bin/python3
"""
Function that writes an Object to a text file, using a JSON.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
