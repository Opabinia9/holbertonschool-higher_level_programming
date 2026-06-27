#!/usr/bin/python3
"""Module: query database with MySQLdb."""

import MySQLdb
from sys import argv


def query_database(
    username: str, password: str, database: str, host: str, port: int
):
    """Query database with given parameters."""
    HOST = host
    PORT = port
    USER = username
    PASS = password
    DB = database
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    query_database(argv[1], argv[2], argv[3], "Localhost", 3306)
