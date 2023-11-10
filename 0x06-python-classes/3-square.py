#!/usr/bin/python3
"""Square Area"""


class Square:
    """Class Square to deal with squares"""

    def __init__(self, size=0):
        """
        Assign square size to private instance attribute

        Args:
            size (int): size of square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size
