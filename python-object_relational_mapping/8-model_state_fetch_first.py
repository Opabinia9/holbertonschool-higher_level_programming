#!/usr/bin/python3
"""Module:."""

from sys import argv
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine(
        f"mysql://{username}:{password}@Localhost:3306/{database}",
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(asc(State.id)).first()
    if result:
        print(result)
    else:
        print("Nothing")
    session.close()
