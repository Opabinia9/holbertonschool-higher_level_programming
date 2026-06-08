#!/usr/bin/python3
"""Module."""

import pickle


class CustomObject:
    """CustomObject."""

    def __init__(self, name: str, age: int, is_student: bool) -> None:
        """Init for CustonObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self) -> None:
        """Print instance atributes."""
        print(
            f"Name: {self.name} Age: {self.age} Is Student: {self.is_student}"
        )

    def serialize(self, filename: str) -> None:
        """Save instance to file."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename: str) -> object:
        """Load instance from file.

        Returns:
            instance of class loaded from file.

        """
        with open(filename, "rb") as file:
            return pickle.load(file)
