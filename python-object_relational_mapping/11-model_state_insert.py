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

    Louisiana = State(name="Louisiana")
    session.add(Louisiana)
    session.commit()

    results = session.query(State).filter(State.name == "Louisiana").first()
    if results:
        print(results.id)
    session.close()
