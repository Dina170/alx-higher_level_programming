#!/usr/bin/python3
"""list 10 commits of a repository by a user (passes as args)
   - must use the GitHub API
   - Print all commits by: `<sha>: <author name>`
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
