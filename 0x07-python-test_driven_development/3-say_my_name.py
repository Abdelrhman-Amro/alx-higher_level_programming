#!/usr/bin/python3
"""print first name and second name"""


def say_my_name(first_name, last_name=""):
    """
        print name

        Args:
            first_name (str): 1st name to print
            last_name (str): 2nd name to print

        Raises:
            TypeError: first_name and last_name must be strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
