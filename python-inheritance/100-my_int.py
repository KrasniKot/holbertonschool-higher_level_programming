#!/usr/bin/python3
"""Contains the class MyInt"""


class MyInt(int):
    """Defines MyInt"""
    def __eq__(self, value):
        """Override the behavior of == operator"""
        return self.real != value

    def __ne__(self, value):
        """Override the behavior of != operator"""
        return self.real == value
