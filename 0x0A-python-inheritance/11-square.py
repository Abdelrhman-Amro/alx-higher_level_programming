#!/usr/bin/python3
"""Define Square class that inherit from BasesGeometry"""
rect = __import__('9-rectangle').Rectangle


class Square(rect):
    """Square Class"""

    def __init__(self, size):
        """
            Constructor

            Args:
                size (int): Side length of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return string"""
        return f"[Square] {self.__size}/{self.__size}"
