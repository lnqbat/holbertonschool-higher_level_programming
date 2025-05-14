#!/usr/bin/python3
"""
That divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    try:
        return [[round(elem / div, 2) for elem in row] for row in matrix]
    except TypeError:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
