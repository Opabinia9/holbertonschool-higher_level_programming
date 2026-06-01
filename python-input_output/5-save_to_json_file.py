#!/usr/bin/python3
"""Module: save_to_json_file."""

import json


def save_to_json_file(my_obj: object, filename: str) -> None:
    """Save object to file in json format."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
