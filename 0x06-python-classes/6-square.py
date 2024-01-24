#!/usr/bin/python3
"""Square module"""


class Square:
    """
    This is the Square class documentation.

    It defines a square with private size and position attributes,
    size validation, getter/setter methods for size and position,
    a method to calculate the area, and a method to print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.
        - position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
        - TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
        - ValueError: If size is less than 0 or if position contains non-positive integers.
        """
        self.size = size
        self.position = position

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

    def __validate_position(self, value=None):
        """
        Validates the position attribute.

        Parameters:
        - value: The value to validate (optional).

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        - ValueError: If position contains non-positive integers.
        """
        if value is not None:
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
                raise ValueError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """
        Getter method to retrieve the position attribute.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position attribute.

        Parameters:
        - value: The new value for the position attribute.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        - ValueError: If position contains non-positive integers.
        """
        self.__validate_position(value)
        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the specified position using the character #.

        If size is equal to 0, prints an empty line.
        Position is used by adding space accordingly.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
