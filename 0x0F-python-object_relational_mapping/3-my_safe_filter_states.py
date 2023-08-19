#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
where `name` matches the argument from the database `hbtn_0e_0_usa`.

But, this time the script is safe from MySQL injections!
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    connect to the database and filter
    results from the database.
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    db = MySQLdb.connect(host="localhost", user=username, port=3306, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '%s' ORDER BY states.id"
    cursor.execute(query, (name,))
    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
