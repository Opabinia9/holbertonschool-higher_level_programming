#!/usr/bin/python3
"""Module: Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """Init for Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs: list = None) -> dict:
        """Return dictionary repisentation of self.

        Returns:
            ...

        """
        if not isinstance(attrs, list):
            return self.__dict__
        if not all(isinstance(x, str) for x in attrs):
            return self.__dict__
        return {x: self.__dict__[x] for x in attrs if x in self.__dict__}

    def reload_from_json(self, json: dict) -> None:
        """Set atters from json."""
        for i, j in json.items():
            setattr(self, i, j)
