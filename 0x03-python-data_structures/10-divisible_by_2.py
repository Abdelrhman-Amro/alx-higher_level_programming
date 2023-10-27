#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [False if x % 2 else True for x in my_list]
    return new_list
