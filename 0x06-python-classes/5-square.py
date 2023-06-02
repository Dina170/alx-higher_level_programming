#!/usr/bin/python3
"""Square Class."""


class Square:
    """Represent a square."""

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
        """update the size value of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return None

        for i in range(1, self.area() + 1):
            print('#', end='')

            if i % self.__size == 0 and i > 0:
                print()
