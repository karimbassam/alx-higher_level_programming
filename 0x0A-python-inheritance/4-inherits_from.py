#!/usr/bin/python3
"""Module for inherits"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.
    
    Args:
        obj: The object to check.
        a_class: The class to compare with.
    
    Returns:
        True if obj is an instance of a class that inherited
        from a_classbut not an instance of a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
