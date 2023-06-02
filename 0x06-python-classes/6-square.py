#!/usr/bin/python3
"""Square Class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the size value of the square.

        Args:
            size (int, optional): The size of the square.
            position (int, int, optional): The position of the square.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
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

    @property
    def position(self):
        """Gets the current position of the square."""
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple or len(position) != 2 \
                or type(position[0]) is not int \
                or type(position[1]) is not int \
                or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
