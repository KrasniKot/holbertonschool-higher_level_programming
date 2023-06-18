#!/usr/bin/python3
"""Creates a class named Square"""


class Square:
    """Defines a Square"""
    def __init__(self, size=0):
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
        """Returns the suqare area"""
        return self.__size**2

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, self2):
        """Equal"""
        return self.area() == self2.area()

    def __ne__(self, self2):
        """Not Equal"""
        return self.area() != self2.area()

    def __gt__(self, self2):
        """Greater Than"""
        return self.area() > self2.area()

    def __ge__(self, self2):
        """Greater or Equal"""
        return self.area() >= self2.area()

    def __lt__(self, self2):
        """Lesser Than"""
        return self.area() < self2.area()

    def __le__(self, self2):
        """Lesser or Equal"""
        return self.area() <= self2.area()
