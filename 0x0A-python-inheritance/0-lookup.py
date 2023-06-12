#!/usr/bin/python3
"""Defines a function that looks for attributes of an objectan"""


def lookup(obj):
    """Return the list of available attributes and methods of an object"""
    return (dir(obj))
