#!/usr/bin/python3
"""Square module"""


class Square:
    """
    This is the Square class documentation.

    It defines a square with a private size attribute, size validation,
    a method to calculate the area, and getter/setter methods for size.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        self.__size = size
        self.__validate_size()

    def __validate_size(self, value=None):
        """
        Validates the size attribute.

        Parameters:
        - value: The value to validate (optional).

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Parameters:
        - value: The new value for the size attribute.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        self.__validate_size(value)
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
