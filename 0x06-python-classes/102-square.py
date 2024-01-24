#!/usr/bin/python3
"""Square module"""


class Square:
    """
    This is the Square class documentation.

    It defines a square with a private size attribute,
    size validation, getter/setter methods for size,
    a method to calculate the area, and comparators based on the square area.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size: The size of the square. Defaults to 0.

        Raises:
        - TypeError: If size is not a number (float or integer).
        - ValueError: If size is less than 0.
        """
        self.size = size

    def __validate_size(self, value=None):
        """
        Validates the size attribute.

        Parameters:
        - value: The value to validate (optional).

        Raises:
        - TypeError: If value is not a number (float or integer).
        - ValueError: If value is less than 0.
        """
        if value is not None:
            if not isinstance(value, (int, float)):
                raise TypeError("size must be a number")
            elif value < 0:
                raise ValueError("size must be >= 0")

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
        - float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Parameters:
        - value: The new value for the size attribute.

        Raises:
        - TypeError: If value is not a number (float or integer).
        - ValueError: If value is less than 0.
        """
        self.__validate_size(value)
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        - float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparator based on square area.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Inequality comparator based on square area.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Less than comparator based on square area.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the area of self is less than the area of other, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Less than or equal to comparator based on square area.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the area of self is less than or equal to the area of other, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Greater than comparator based on square area.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the area of self is greater than the area of other, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Greater than or equal to comparator based on square area.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the area of self is greater than or equal to the area of other, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
