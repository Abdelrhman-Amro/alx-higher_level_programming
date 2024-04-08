#!/usr/bin/python3
"""
sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib import request as req, error as err
    from sys import argv
    
    try:
        with req.urlopen(argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except err.HTTPError as er:
        print('Error code:', er.code)
