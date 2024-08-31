#!/usr/bin/python3
"""
Module defining the Rectangle class.
"""


class Rectangle:
    """Define a rectangle with width and height."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = Rectangle.print_symbol
        if isinstance(symbol, str):
            return "\n".join([symbol * self.__width] * self.__height)
        elif isinstance(symbol, int):
            symbol = str(symbol)
            return "\n".join([symbol * self.__width] * self.__height)
        elif isinstance(symbol, list):
            rows = []
            symbol_length = len(symbol)
            for i in range(self.__height):
                row = "".join(str(symbol[j % symbol_length]) for j in range(self.__width))
                rows.append(row)
            return "\n".join(rows)
        else:
            raise TypeError("print_symbol must be a string, integer, or list")

    def __repr__(self):
        """Return a string representation of the rectangle for eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
