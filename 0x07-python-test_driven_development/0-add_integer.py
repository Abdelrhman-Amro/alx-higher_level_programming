#!/usr/bin/python3
"""Return summation of two numbers"""


def add_integer(a, b=98):
    """
        Add two numbers

        Args:
            a (int) or (float): First Number
            b (int) or (float): Second Number
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return a + b
