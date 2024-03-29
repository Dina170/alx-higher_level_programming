#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
