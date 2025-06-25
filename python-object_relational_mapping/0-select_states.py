#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def main():
    """
    that lists all states
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()