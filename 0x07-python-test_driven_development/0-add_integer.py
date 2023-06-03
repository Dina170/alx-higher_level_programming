#!/usr/bin/python3
"""A module to add two numbers"""


def add_integer(a, b=98):
    """Adds two numbers

    Performs the addition between two numbers.

    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number.

    Returns:
        int: The result of the addition.

    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return (int(a) + int(b))
