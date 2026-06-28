"""Module: create states table."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """States table."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=True)
    name = Column(String(128), nullable=False)
