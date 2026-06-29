#!/usr/bin/python3
"""Module:."""

from sys import argv
from sqlalchemy import create_engine, delete
from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine(
        f"mysql://{username}:{password}@Localhost:3306/{database}",
    )

    # Write a script that deletes all State objects with a
    # name containing the letter a from the database hbtn_0e_6_usa

    Session = sessionmaker(bind=engine)
    with Session() as session:
        stmt = delete(State).where(State.name.like("%a%"))
        session.execute(stmt)
        session.commit()
