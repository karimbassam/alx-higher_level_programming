#!/usr/bin/python3
"""Module for add_integer"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a: The first number, expected to be an integer or a float.
    b: The second number, expected to be an integer or a float. Defaults to 98.

    Returns:
    The sum of a and b as an integer

    Raises:
    TypeError: If either a or b is not integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats and perform the addition
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
