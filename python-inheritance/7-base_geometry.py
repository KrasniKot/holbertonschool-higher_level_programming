#!/usr/bin/python3
"""Contains the class BaseGeometry"""


class BaseGeometry:
    """
    class Basegeometry definition
    """

    def area(self):
        """rasies an exception exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
