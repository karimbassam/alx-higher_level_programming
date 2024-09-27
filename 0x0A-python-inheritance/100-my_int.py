#!/usr/bin/python3
"""Module for MyInt"""


class MyInt(int):
    """A class that inherits from int but inverts == and != operators."""

    def __eq__(self, other):
        """Override == operator with != behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator with == behavior."""
        return super().__eq__(other)
