#!/usr/bin/python3
"""Contains the class BaseGeometry"""


class BaseGeometry:
    """class Basegeometry definition"""

    def area(self):
        """rasies an exception exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
