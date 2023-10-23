#!/usr/bin/python3


for i in range(90, 64, -1):
    x = i
    if not i % 2:
        x = i + 32
    print("{:c}".format(x), end="")
