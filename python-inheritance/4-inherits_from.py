#!/usr/bin/python3
"""Function inherits_from()"""


def inherits_from(obj, a_class):
    """
    Determines if an object is instance of a class
    that inherited (directly or not)
    """
    return isinstance(obj, a_class) and type(obj) != a_class
