#!/usr/bin/python3
"""A module to divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (:obj:`list` of :obj:`list`): The matrix to be divided.
        div (int): The divisor number.

    Returns:
        list: A new matrix with all elements divided.

    Raises:
        TypeError: If `matrix` list of lists of integers or floats or
            if `div` is not a number.
        ZeroDivisionError: If `div` is equal to `0`.

    """

    new_matrix = []
    new_list = []
    list_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(list_error)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(list_error)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
