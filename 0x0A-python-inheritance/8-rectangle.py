#!/usr/bin/python3
"""Define Rectangle class that inherit from BasesGeometry"""
BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """Rectangle Class"""

    def __init__(self, width, height):
        """
            Constructor

            Args:
                Width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
