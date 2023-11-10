#!/usr/bin/python3
"""Square Area"""


class Square:
    """Class Square to deal with squares"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Assign square size to private instance attribute

        Args:
            size (int): size of square
            posisition (int, int): spaces before print square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size -> GET/SET"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position -> GET/SET"""
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2
                and isinstance(value[0], int) and isinstance(value[1], int)
                and value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print Square with # sympol"""

        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for j in range(self.__size)]
                print()
