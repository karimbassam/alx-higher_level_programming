#!/usr/bin/python3
"""Module for Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class that defines a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new rectangle.

        Args:
            width (int): The width of rectangle (must be positive integer)
            height (int): The height of rectangle(must be positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
