#!/usr/bin/python3
"""Define Square class that inherit from BasesGeometry"""
BG = __import__('7-base_geometry').BaseGeometry


class Square(BG):
    """Square Class"""

    def __init__(self, size):
        """
            Constructor

            Args:
                size (int): Side length of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size
