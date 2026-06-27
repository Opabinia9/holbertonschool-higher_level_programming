#!/usr/bin/python3
"""Module: query database with MySQLdb."""

import MySQLdb
import sys

if __name__ == "__main__":
    ""
    HOST = "Localhost"
    PORT = 3306
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    result = cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
