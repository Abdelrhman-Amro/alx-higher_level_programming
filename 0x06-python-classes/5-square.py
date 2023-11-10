#!/usr/bin/python3
"""Square Area"""


class Square:
    """Class Square to deal with squares"""

    def __init__(self, size=0):
        """
        Assign square size to private instance attribute

        Args:
            size (int): size of square
        """
        self.size = size

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

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

    def my_print(self):
        """Print Square with # sympol"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
