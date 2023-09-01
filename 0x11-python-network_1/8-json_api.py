#!/usr/bin/python3
"""Takes in a letter and sends a POST request
   to `http://0.0.0.0:5000/search_user` with the letter as a parameter
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    payload = {'q': q}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', payload).json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print('Not a valid JSON')
