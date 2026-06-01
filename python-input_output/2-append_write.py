#!/usr/bin/python3
"""Module: append_write."""


def append_write(filename: str = "", text: str = "") -> int:
    """Append a string to the end of a file.

    Returns:
        ...

    """
    with open(filename, "a", encoding="utf") as file:
        return file.write(text)
