#!/usr/bin/python3
"""Takes in a URL and an email,
   sends a POST request to the passed URL with the email as a parameter,
   and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    values = {"email": argv[2]}
    data = urllib.parse.urlencode(values).encode("ascii")

    request = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
