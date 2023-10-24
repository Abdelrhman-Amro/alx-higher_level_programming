#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    narg = len(argv)
    if narg < 2:
        print("0 arguments.")
    elif narg == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(narg-1))
        for i in range(1, narg):
            print("{}: {}".format(i, argv[i]))
