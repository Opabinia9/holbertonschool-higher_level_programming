#!/usr/bin/python3
"""Module."""


class Student:
    """Class."""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """M."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self) -> dict:
        """J.

        Returns:
            pass

        """
        return self.__dict__
