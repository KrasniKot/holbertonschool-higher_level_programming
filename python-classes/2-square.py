#!/usr/bin/python3
"""Creates a class named Square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """
        Initializes a Square
        Atributtes:
            size: Square size.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
