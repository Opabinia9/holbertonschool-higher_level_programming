#!/usr/bin/python3
"""Module:."""


def class_to_json(obj: object) -> dict:
    """Return the __dict__ of an object.

    Returns:
        the __dict__ of an object

    """
    return obj.__dict__
