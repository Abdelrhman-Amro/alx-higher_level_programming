#!/usr/bin/python3
"""Rectangle Area"""


class Rectangle:
    """CLASS TO DEAL WITH RECTANGLE"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Consturctor to set initial values

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __del__(self):
        """Detect instance deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def height(self):
        """GET/SET height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """GET/SET width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the rectangle perimeter"""
        H = self.__height
        W = self.__width
        return (H + W) * 2 if H and W else 0

    def __str__(self):
        """Return rectangle to print"""
        S = []
        if not (self.__height and self.__width):
            return "".join(S)
        for j in range(self.__height):
            [S.append(str(self.print_symbol)) for i in range(self.__width)]
            if j + 1 != self.__height:
                S.append("\n")
        return "".join(S)

    def __repr__(self):
        """
            turn a string representation of the rectangle
            to be able to recreate a new instance
            by using eval()
        """
        new_rect = "Rectangle(" + str(self.__width) + ", "
        new_rect += str(self.__height) + ")"
        return new_rect
