#!/usr/bin/python3
"""Module: create states table."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """States table."""

    __tablename__ = "states"
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"{self.id}: {self.name}"
