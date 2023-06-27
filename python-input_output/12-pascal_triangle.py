#!/usr/bin/python3
"""Contains pascal_triangle()"""


def pascal_triangle(n):
    """Returns a list of lists representing the Pascal's triangle"""
    tri = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(tri[-1][j:j + 2]))
        tri.append(row)
    return tri
