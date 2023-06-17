#!/usr/bin/python3
"""A module which contains the class rectangle"""


class Rectangle:
    """Definition of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of an instance"""

        self.__width = width
        self.__height = height

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
            self.__height = vailue
