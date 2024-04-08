#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
The letter must be sent in the variable q
"""
if __name__ == "__main__":
    from requests import post as POST
    from sys import argv

    username = argv[1]
    password = argv[2]
