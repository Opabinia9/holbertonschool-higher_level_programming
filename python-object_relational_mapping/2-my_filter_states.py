#!/usr/bin/python3
"""Module: query database with MySQLdb."""

import MySQLdb
from sys import argv


def query_database(username: str, password: str, database: str, state_name):
    """Query database with given parameters."""
    HOST = "Localhost"
    PORT = 3306
    USER = username
    PASS = password
    DB = database
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    query_database(argv[1], argv[2], argv[3], argv[4])
