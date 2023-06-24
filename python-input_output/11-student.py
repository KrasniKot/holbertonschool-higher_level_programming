#!/usr/bin/python3
"""Contains Student class"""


class Student:
    """Defines a Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of Student"""
        if attrs:
            new_attrs = {}
            for at in attrs:
                if at in self.__dict__:
                    new_attrs[at] = self.__dict__[at]
            return new_attrs
        return self.__dict__
