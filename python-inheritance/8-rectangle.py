#!/usr/bin/python3
"""Module."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectange inherites from BaseGeometry."""

    def __init__(self, width: int, height: int) -> None:
        """Init from Rectange."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
