#!/usr/bin/python3
"""Define lookup function"""


def lookup(obj):
    """
        Return the list of available attributes and methods of an object

        Args:
        obj (object): Object from any type
    """
    return dir(obj)
