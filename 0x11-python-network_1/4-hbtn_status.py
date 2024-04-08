#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    from requests import get as GET

    url = "https://alx-intranet.hbtn.io/status"
    rsp = GET(url)
    print("Body response:")
    print(f"\t- type: {type(rsp.text)}")
    print(f"\t- content: {rsp.text}")
