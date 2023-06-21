#!/usr/bin/python3
"""Contains MyList class"""


class MyList(list):
    """
    MyList class definition
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        """
        print(sorted(self))
