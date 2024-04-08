#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response.
"""
if __name__ == "__main__":
    from requests import post as POST
    from sys import argv

    url = argv[1]
    email = argv[2]

    params = {'email': email}
    rsp = POST(url, data=params)
    print(rsp.text)
