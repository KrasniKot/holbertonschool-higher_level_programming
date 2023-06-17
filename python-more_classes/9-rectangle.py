#!/usr/bin/python3
"""A module which contains the class rectangle"""


class Rectangle:
    """Definition of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of an instance"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Returns the rectangle representation for print() and str()"""
        rect = ""
        if self.__width > 0 and self.width > 0:
            for y in range(self.__height):
                for x in range(self.__width):
                    rect += str(self.print_symbol)
                rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """Returns the rectangle representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new instance of the class"""
        return cls(size, size)
