#!/usr/bin/python3
"""Module:."""

import csv
import json


def convert_csv_to_json(csv_filename: str, newline="") -> None:
    """Convert a csv file to a json file"""
    with open(csv_filename, "r", newline="") as file:
        data = list(csv.DictReader(file))
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
