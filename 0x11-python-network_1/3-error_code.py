#!/usr/bin/python3
"""
sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request as req, error as er

    try:
        with req.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except er.HTTPError as erno:
        print('Error code:', erno.code)
