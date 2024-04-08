#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""
if __name__ == "__main__":
    from requests import get as GET
    import requests
    from sys import argv

    url = argv[1]
    rsp = GET(url)
    if rsp.status_code >= 400:
        print("Error code: {}".format(rsp.status_code))
    else:
        print(rsp.text)
