#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cur = db.cursor()

    query = ("""SELECT * FROM states WHERE BINARY name = '{}'
        ORDER BY id ASC""".format(state_name))
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
