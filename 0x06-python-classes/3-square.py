#!/usr/bin/python3
"""Square module"""


class Square:
    """
    This is the Square class documentation.

    It defines a square with a private size attribute, size validation,
    and a method to calculate the area.
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

    def __validate_size(self):
        """
        Validates the size attribute.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
