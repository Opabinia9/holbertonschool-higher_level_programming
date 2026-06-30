#!/usr/bin/python3
"""Module:."""

from sys import argv
from sqlalchemy import create_engine, select, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database}",
    )

    Session = sessionmaker(bind=engine)
    with Session() as session:
        stmt = (
            select(State.name, City.id, City.name)
            .join(State, City.state_id == State.id, isouter=True)
            .order_by(asc(City.id))
        )
        results = session.execute(stmt)
        for result in results:
            print("{}: ({}) {}".format(*result))
