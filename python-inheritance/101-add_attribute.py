#!/usr/bin/python3
"""Contains add_attribute()"""


def add_attribute(Obj, attr, val):
    """Adds an attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
