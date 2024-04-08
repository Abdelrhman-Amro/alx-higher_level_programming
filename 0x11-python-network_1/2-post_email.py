#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    from urllib import request as req, parse as p
    from sys import argv

    url = argv[1]
    email = argv[2]

    data = {"email": email}
    encoded_data = p.urlencode(data).encode('utf-8')
    Req = req.Request(url, encoded_data, method='POST')
    
    with req.urlopen(Req) as rsp:
        print(rsp.read().decode('UTF-8'))
