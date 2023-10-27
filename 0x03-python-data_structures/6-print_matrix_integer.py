#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        ln = len(row)
        if not ln:
            print()
        for idx in range(ln):
            print("{:d}".format(row[idx]), end="\n" if idx == ln - 1 else " ")
