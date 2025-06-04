#!/usr/bin/env python3
"""
That adds the functionality to serialize a Python dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary and saves it.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    pass


def load_and_deserialize(filename):
    """
    Loads and deserializes a dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
    pass
