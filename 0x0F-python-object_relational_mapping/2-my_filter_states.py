#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
where `name` matches the argument from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    connect to the database and filter
    results from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE BINARY name = '{}' \
                 ORDER BY states.id".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
