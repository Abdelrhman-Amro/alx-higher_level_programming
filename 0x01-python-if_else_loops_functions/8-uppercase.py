#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        if (i >= 97 and i <= 123):
            i -= 32
        print("{:c}".format(i), end="")
    print("")
