#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        ln = len(row)
        for idx in range(ln):
            print("{:d}".format(row[idx]), end="" if idx == ln - 1 else " ")
        print()
