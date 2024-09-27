#!/usr/bin/python3
"""Module for Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to represent a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new rectangle.

        Args:
            width (int): The width of rectangle (must be positive integer)
            height (int): The height of rectangle (must be positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description in the
        format [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
