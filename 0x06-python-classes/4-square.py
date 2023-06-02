#!/usr/bin/python3
class Square:
    """Square Class."""

    def __init__(self, size=0):
        """initializes the size value of the square.

        Args:
            size (:obj:`int`, optional): The size of the square.

        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the current size of the square."""
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
