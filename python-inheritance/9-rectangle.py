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

    def area(self) -> int:
        """Area of Rectangle.

        Returns:
            The area of rectangle

        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """Str of Rectangle.

        Returns:
            description of Rectangle.

        """
        return f"[Rectangle] {self.__width}/{self.__height}"
