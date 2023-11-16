#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    divide list of numbers by div

    Args:
        matrix (list): 2d list of integers of floats
        div (int or float): number to divide matrix by

    Returns:
        list: new matrix

    Raises:
        TypeError: matrix must be a list of lists of integers or floats
        TypeError: Each row of the matrix must be of the same size
        TypeError: div must be a number (integer or float)
        ZeroDivisionError: div can't be equal to 0
    """
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix"
                            "(list of lists) of integers/floats")
        for x in row:
            if not (isinstance(x, int) or isinstance(x, float)):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
    sz = len(matrix[0])
    for i in matrix[1:]:
        if len(i) != sz:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
