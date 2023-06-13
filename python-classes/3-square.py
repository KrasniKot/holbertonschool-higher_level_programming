#!/usr/bin/python3
"""Creates a class named Square"""


class Square:
    """Defines a Square"""
    def __init__(self, size):
        """
        Initializes an square
        Atrbuttes:
            size: square size.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        return self.__size**2
