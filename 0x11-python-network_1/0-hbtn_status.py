#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    data = response.read()
    print("Body response:")
    print(f"\t- type: <class '{type(data)}'>")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data.decode('utf-8')}")

