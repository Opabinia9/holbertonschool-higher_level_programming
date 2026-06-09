#!/usr/bin/python3
"""Module:."""

import csv
import json


def convert_csv_to_json(csv_filename: str, newline="") -> bool:
    """Convert a csv file to a json file.

    Returns:
        True on success else False

    """
    try:
        with open(csv_filename, "r", newline="") as file:
            data = list(csv.DictReader(file))
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception:
        return False
