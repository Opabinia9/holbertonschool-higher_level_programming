#!/usr/bin/python3
"""Module: from_json_string."""

import json


def from_json_string(my_str):
    """Convert a json string to python object.

    Returns:
        a python object

    """
    return json.loads(my_str)
