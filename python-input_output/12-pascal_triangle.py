#!/usr/bin/python3
"""Contains pascal_triangle()"""


def pascal_triangle(n):
    """Returns a list of lists representing the Pascal's triangle"""
    tri = []
    for i in range(n):
        tri += [list(str(11**i))]
    return tri
