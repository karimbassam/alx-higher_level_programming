#!/usr/bin/python3
"""
Module for LockedClass.
This module defines a LockedClass that only allows setting
'first_name' as an attribute.
"""


class LockedClass:
    """
    A class that prevents the dynamic creation of new attributes,
    except for the attribute 'first_name'.
    """
    __slots__ = ['first_name']
