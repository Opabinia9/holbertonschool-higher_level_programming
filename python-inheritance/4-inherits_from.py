#!/usr/bin/python3
"""Module: inherits_from."""


def inherits_from(obj, a_class):
    """Check if obj is from a subclass of a_class, excluding a_class.

    Returns:
        Boolean

    """
    return isinstance(obj, a_class) and type(obj) is not a_class
