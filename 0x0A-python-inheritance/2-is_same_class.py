#!/usr/bin/python3
"""Define is_same_class function"""


def is_same_class(obj, a_class):
    """
        Return True if the object is exactly an instance of the specified class
        otherwise False

        obj (any): variable to check type
        a_class (type): the class to check with obj

        Return:
            bolean: True if the object is exactly instance of specified class
            bolean: otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
