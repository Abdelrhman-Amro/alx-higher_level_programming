#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
The letter must be sent in the variable q
"""
if __name__ == "__main__":
    from requests import post as POST
    from sys import argv

    if len(argv) == 1:
        value = ""
    else:
        value = argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': value}
    rsp = POST(url, data=payload)

    try:
        j = rsp.json()
        if j == {}:
            print("No result")
        else:
            print(f"[{j.get('id')}] {j.get('name')}")
    except ValueError:
        print("Not a valid JSON")
