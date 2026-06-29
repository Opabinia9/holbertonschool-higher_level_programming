#!/usr/bin/python3
"""Module: create city table."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    """cities table."""

    __tablename__ = "cities"
    id = Column(
        "id", Integer, unique=True, autoincrement=True, primary_key=True
    )
    name = Column("name", String(128), nullable=False)
    state_id = Column(
        "state_id", Integer, ForeignKey("states.id"), nullable=False
    )

    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"{self.id}: {self.name}"
