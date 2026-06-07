#!/usr/bin/python3
"""Moudle."""

import json


def serialize_and_save_to_file(data: dict, filename: str) -> None:
    """Serialize and save data to the specified file."""
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename: str) -> dict:
    """Load and deserialize data from the specified file.

    Returns:
        python dictionary generated from file

    """
    with open(filename, "r") as file:
        return json.load(file)
