#!/usr/bin/python3
"""Module: write_file."""


def write_file(filename: str = "", text: str = "") -> int:
    """Write text to a file.

    Returns:
        number of characters written

    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
