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
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
    cursor.execute(query, (argv[4],))
    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
