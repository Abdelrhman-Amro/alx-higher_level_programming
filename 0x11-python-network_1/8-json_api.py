#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
The letter must be sent in the variable q
"""
if __name__ == "__main__":
    from requests import post as POST
    from sys import argv

    if len(argv) > 1:
        value = argv[1]
    else:
        value = ""

    url = "http://0.0.0.0:5000/search_use"
    params = {'q': value}
    rsp = POST(url, data=params)

    try:
        j = rsp.json()
        if j is {}:
            print('No result')
        else:
            print(f"[{j.get('id')}] {j.get('name')}")
    except:
        print("Not a valid JSON")   
