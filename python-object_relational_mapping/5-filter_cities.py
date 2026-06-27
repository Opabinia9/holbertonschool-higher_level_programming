#!/usr/bin/python3
"""Module: query database with MySQLdb."""

import MySQLdb
from sys import argv


def query_database(
    username: str, password: str, database: str, state_name: str
) -> None:
    """Query database with given parameters."""
    db = MySQLdb.connect(
        host="Localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )
    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,),
    )
    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    query_database(argv[1], argv[2], argv[3], argv[4])
