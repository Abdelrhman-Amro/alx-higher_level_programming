#!/usr/bin/python3
"""Define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj isinstance of class

     Args:
        obj (any): variable to check type
        a_class (type): class to check matching with obj

    Return:
        bolean: True -> if the object is an instance of
                        or if the object is an instance of a class
                        that inherited from, the specified class
        bolean: false -> Otherwise
    """
    return isinstance(obj, a_class)
