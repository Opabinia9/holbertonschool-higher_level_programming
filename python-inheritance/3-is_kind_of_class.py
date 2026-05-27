#!/usr/bin/python3
"""Module: is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Return if obj is from a_class.

    Returns:
        True if obj is an instance of a_class, else False

    """
    return True if isinstance(obj, a_class) else False
