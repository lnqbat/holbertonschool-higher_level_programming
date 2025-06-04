#!/usr/bin/python3
"""
Serialize and deserialize custom Python objects using the pickle module.
"""


import pickle


class CustomObject:
    """
    Define a class
    """
    def __init__(self, name, age, is_student):
        """
        Ini class.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                obj = pickle.dump(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            pass
        return None
