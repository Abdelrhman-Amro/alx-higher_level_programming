#!/usr/bin/python3
import requests

"""payload = {'key11gsdf gasdfg fasfg234': 'dafsdfa sdfasdf asd fagf gafdgafvalue1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.text)
print(r.json())"""

r = requests.get('https://example.com/')
print(r.text)
print(r.json())
