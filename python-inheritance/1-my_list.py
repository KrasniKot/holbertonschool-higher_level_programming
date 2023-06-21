#!/usr/bin/python3
"""Module which contains MyList class"""


class MyList(list):
    """MyList class definition"""

    def print_sorted(self):
        """prints the list sorted"""
        print(sorted(self))
