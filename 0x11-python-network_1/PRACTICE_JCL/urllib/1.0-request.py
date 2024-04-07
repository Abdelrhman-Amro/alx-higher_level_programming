#!/usr/bin/env python3
from urllib import request as req

# Open url
rsp = req.urlopen("https://example.com/")

print(f"What is habben after request🤷 --\"type\"--> {type(rsp)}")
print("-----------------------------------------\n")
# Link Of this type:-> https://docs.python.org/3/library/http.client.html#httpresponse-objects
print(f"What is inside The response:\n{dir(rsp)}")
print("-----------------------------------------\n")

print(f"rsp code: ", rsp.code)
print(f"rsp length: ", rsp.length)
# look at small part of the response, rather than the full value.
print("look at small part of the response, rather than the full value:\n", rsp.peek())
print("-----------------------------------------\n")

data = rsp.read()
print("The type of data is: ", type(data))
print("FULL DATA in (bytes):\n", data)
print("-----------------------------------------\n")

str = data.decode("utf-8")
print("The type of data is: ", type(str))
print("FULL DATA in (str):\n", str)
print("-----------------------------------------\n")

# 😔Once you read the response python close the connection
print("😔😔Try to read again😔😔: ", rsp.read())
