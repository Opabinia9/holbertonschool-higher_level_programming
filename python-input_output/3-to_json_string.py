#!/usr/bin/python3
"""Module: to_json_string."""

import json


def to_json_string(my_obj: object) -> str:
    """Convert an object to a json string.

    Returns:
        a json string

    """
    return json.dumps(my_obj)
