#!/usr/bin/python3
"""Module: ."""

import json


def load_from_json_file(filename: str) -> object:
    """Create object from json file.

    Returns:
        an object

    """
    with open(filename) as file:
        return json.load(file)
