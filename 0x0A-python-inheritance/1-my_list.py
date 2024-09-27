#!/usr/bin/python3
"""Module for list"""


class MyList(list):
    """A custom list class that inherits from the built-in list class.

    This class has a method to print the list elements sorted in ascending order.
    """

    def print_sorted(self):
        """Prints the list elements in ascending order without modifying the original list."""
        print(sorted(self))

