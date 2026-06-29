#!/usr/bin/python3
"""Module:."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy import update
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
    with Session() as session:
        stmt = update(State).where(State.id == 2).values(name="New Mexico")
        session.execute(stmt)
        session.commit()
