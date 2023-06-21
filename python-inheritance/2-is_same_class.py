#!/usr/bin/python3
"""Function is_same_class"""


def is_same_class(obj, a_class):
    """function which checks for obj to be the type(a_class)"""
    if type(obj) == a_class:
        return True
    return False
