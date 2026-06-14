#!/usr/bin/python3
"""Module."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class, inherites from Rectangle class."""

    def __init__(self, size: int) -> None:
        """Init for Square."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        """Area of Square.

        Returns:
            The area of the square

        """
        return self.__size**2
