#!/usr/bin/python3
"""Module of is kind"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or inherits from a_class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is an instance or inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
