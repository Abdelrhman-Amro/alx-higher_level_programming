#!/usr/bin/python3
"""print square of #"""


def print_square(size):
    """
        print square

        Args:
            size (int): length of the side

        Raises:
            TypeError: size must be an integer
            ValueError: if size is less than 0
            TypeError: if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
