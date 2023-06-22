#!/usr/bin/python3
"""Contains the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a Rectangle
    """

    def __init__(self, width, height):
        """Rectangle initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Deines the output when print() or str() called"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of a Rectangle"""
        return self.__width*self.__height
