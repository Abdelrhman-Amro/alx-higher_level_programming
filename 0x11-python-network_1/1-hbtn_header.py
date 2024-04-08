#!/usr/bin/python3
"""
and displays the value of the X-Request-Id variable
found in the header of the response.
"""


if __name__ == "__main__":
    from urllib import request as req
    from sys import argv

    with req.urlopen(argv[1]) as rsp:
        print(rsp.getheader('X-Request-Id'))
