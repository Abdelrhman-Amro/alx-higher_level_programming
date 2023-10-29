#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys_list = sorted(a_dictionary)
    [print("{:s}: {}".format(k, a_dictionary[k])) for k in sorted_keys_list]
