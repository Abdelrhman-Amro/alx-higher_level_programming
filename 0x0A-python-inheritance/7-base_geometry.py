#!/usr/bin/python3
"""Define BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validate value

            Args:
                name (string): is the name
                value (int): value of the name

            Raises:
                TypeError: if value != int
                ValueError: if value < 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
