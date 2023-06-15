#!/usr/bin/python3
"""
Function which adds to integers:
    a + b
    or int(a) + int(b)
"""


def add_integer(a, b=98):
    """
    Adds two integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
