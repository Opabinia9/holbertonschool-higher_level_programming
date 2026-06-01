#!/usr/bin/python3
"""Module: read_file."""


def read_file(filename: str = "") -> None:
    """Print contents of a file."""
    with open(filename, encoding="utf-8") as file:
        text = file.read()
        print(text)
