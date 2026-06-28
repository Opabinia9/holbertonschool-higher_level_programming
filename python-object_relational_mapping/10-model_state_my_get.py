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
    state_name = argv[4]
    engine = create_engine(
        f"mysql://{username}:{password}@Localhost:3306/{database}",
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State)
        .filter(State.name == state_name)
        .order_by(asc(State.id))
        .first()
    )
    if results:
        print(results.id)
    else:
        print("Not found")
    session.close()
