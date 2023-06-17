#!/usr/bin/python3
"""A module which contains the class rectangle"""


class Rectangle:
    """Definition of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of an instance"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width*self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width+self.__height)

    def __str__(self):
        rect = ""
        if self.__width > 0 and self.width > 0:
            for y in range(self.__height):
                for x in range(self.__width):
                    rect += "#"
                rect += "\n"
        return rect[:-1]
