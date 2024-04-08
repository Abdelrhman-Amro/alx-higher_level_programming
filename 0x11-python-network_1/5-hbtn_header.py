#!/usr/bin/python3
"""
sends a request to the URL and displays
the value of the variable X-Request-Idin the response header
"""
if __name__ == "__main__":
    from requests import get as GET
    from sys import argv

    url = argv[1]
    rsp = GET(url)
    print(rsp.headers.get('X-Request-Id'))
