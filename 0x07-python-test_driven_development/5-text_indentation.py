#!/usr/bin/python3
"""

This module prints a text with a 2 new lines after each of
these characters: `.`, `?`, `:`

"""


def text_indentation(text):
    """

    Prints a text with indentation

    Args:
        text (str): The text to prints.

    Raises:
        TypeError: If `text` isn't string.

    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    text_length = len(text)
    idx = 0

    while idx < text_length and text[idx] == ' ':
        idx += 1

    while idx < text_length:
        print(text[idx], end="")
        if text[idx] == "\n" or text[idx] in ".?:":
            if text[idx] in ".?:":
                print("\n")
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue
        idx += 1
