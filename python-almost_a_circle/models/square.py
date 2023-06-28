#!/usr/bin/python3
from models.rectangle import Rectangle
"""Contains class Square"""


class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the inherited __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
