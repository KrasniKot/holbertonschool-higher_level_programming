#!/usr/bin/python3
"""
Divides each element of a matrix by div.
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix and returns the result
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(error)

    for elist in matrix:
        if any(type(el) != int and type(el) != float for el in elist)\
                or len(elist) == 0:
            raise TypeError(error)

    if any(len(matrix[0]) != len(elist) for elist in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float or div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el/div, 2) for el in elist]for elist in matrix]
