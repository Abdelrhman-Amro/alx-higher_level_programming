#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """
        class inherit from list

        Methods:
            print_sorted(): print sorted list
    """

    def print_sorted(self):
        """print list in ascending order"""
        Sorted_list = sorted(self)
        print(Sorted_list)
