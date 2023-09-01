#!/usr/bin/python3
"""Takes in a URL and an email,
   sends a POST request to the passed URL with the email as a parameter,
   and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import requests


if __name__ == "__main__":
    values = {"email": argv[2]}

    r = requests.post(argv[1], data=values)
    print(r.text)
