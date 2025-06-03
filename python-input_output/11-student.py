#!/usr/bin/python3
"""
Write a class Student that defines a student.
"""


class Student:
    """
    Init a class student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        That retrieves a dictionary representation
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if isinstance(attr, str):
                    if attr in self.__dict__:
                        result[attr] = self.__dict__[attr]
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        That replaces all attributes of the Student instance.
        """
        for key in json:
            self.__dict__[key] = json[key]
