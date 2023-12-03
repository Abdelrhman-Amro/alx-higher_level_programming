#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (any): variable to check type
        a_class (type): class to check matching with obj

    Return:
        bolean: True if the check is true
        bolean: Fals otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
