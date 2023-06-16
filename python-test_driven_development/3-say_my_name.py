#!/usr/bin/python3
"""Prints the fist and the last name"""


def say_my_name(first_name, last_name=""):
    """
    "My name is:" followed by the first and the last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))