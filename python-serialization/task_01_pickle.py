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
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

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
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
        except Exception:
            return None

        if type(obj) is not cls:
            return None

        return obj
