#!/usr/bin/python3
"""list 10 commits of a repository by a user (passes as args)
   - must use the GitHub API
   - Print all commits by: `<sha>: <author name>`
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])).json()
    for i in range(10):
        print("{}: {}".format(r[i].get("sha"),
                              r[i].get("commit").get("author").get("name")))
