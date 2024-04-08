#!/usr/bin/python3
import requests

r = requests.get('https://httpbin.org/json')
print(r.text)

# Check if the response content is in JSON format
if "application/json" in r.headers["Content-Type"]:
    for item in r.json():
        print(item)
else:
    print("Response content is not in JSON format.")
