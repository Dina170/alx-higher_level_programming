#!/usr/bin/python3
"""
lists all cities from
the database `hbtn_0e_4_usa`.
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
    cur.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities \
                   JOIN states \
                     ON cities.state_id = states.id \
                  ORDER BY cities.id")

    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
