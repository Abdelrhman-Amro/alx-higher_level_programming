#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request as req

    with req.urlopen("https://alx-intranet.hbtn.io/status") as rsp:
        x = rsp.read()
        print("Body response:")
        print(f"\t- type: {type(x)}")
        print(f"\t- content: {x}")
        print(f"\t- utf8 content: {x.decode('UTF-8')}")
