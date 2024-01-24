#!/usr/bin/python3
"""Magic module"""


import math

class MagicClass:
    """
    MagicClass represents a magical class with the power of calculations based on radius.

    Attributes:
    - __radius (float): The radius of the magic circle.

    Methods:
    - __init__(self, radius=0): Initializes a new MagicClass instance with a specified radius.
    -area(self): Calculates and returns the area of the magic circle.
    -circumference(self): Calculates and returns the circumference of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance with a specified radius.

        Parameters:
        -radius (float, optional): The radius of magic circle. Defaults to 0

        Raises:
        - TypeError: If the provided radius is not a number (float or integer).
        """
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle.

        Returns:
        - float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the magic circle.

        Returns:
        - float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
