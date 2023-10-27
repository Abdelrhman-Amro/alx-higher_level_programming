#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None

    MX = my_list[0]
    for n in my_list:
        if n > MX:
            MX = n
    return MX
