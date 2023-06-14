#!/usr/bin/python3
"""Creates a class named Square"""


class Square:
    """Defines a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an square
        Atrbuttes:
            size: square size.
            position: tuple.
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints a square using '#'"""
        if self.__size == 0:
            print()
        else:
            for l in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """position getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter method"""
        if type(value) != tuple or len(value) != 2 or type(i) != int for i in value:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
