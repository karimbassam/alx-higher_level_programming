#!/usr/bin/python3
"""Module for square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class to represent a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the square (must be a positive integer).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
