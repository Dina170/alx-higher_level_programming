#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    temp = []
    res = []
    triangle = []
    for i in range(n):
        if len(temp) > 1:
            for j in range(len(temp) - 1):
                res[j + 1] = temp[j + 1] + temp[j]
        res.append(1)
        temp = list(res)
        triangle.append(temp)

    return triangle
