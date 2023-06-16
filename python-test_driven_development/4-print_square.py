#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """
    prints a square
    """
    if type(size) != int or type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(size):
        for x in range(size):
            print("#", end="")
        print()
