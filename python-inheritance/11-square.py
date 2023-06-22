#!/usr/bin/python3
"""Contains the class Square"""
pc = __import__('9-rectangle').Rectangle


class Square(pc):
    """
    Defines a Square
    """

    def __init__(self, size):
        """Initializes a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string"""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Returns the Square area"""
        return self.__size**2
