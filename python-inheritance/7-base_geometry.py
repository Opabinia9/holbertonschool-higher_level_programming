#!/usr/bin/python3
"""Module: BaseGeomtry."""


class BaseGeometry:
    """Class: empty base class."""

    def area(self):
        """C.

        Raises:
            Exception: until function is finished

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer.

        Raises:
            TypeError: if value is not and integer
            ValueError: if value is not greater then zero

        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
