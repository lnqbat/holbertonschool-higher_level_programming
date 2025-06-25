#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
with their associated state names, ordered by cities.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
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
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
