#!/usr/bin/python3
"""define read_file function"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
