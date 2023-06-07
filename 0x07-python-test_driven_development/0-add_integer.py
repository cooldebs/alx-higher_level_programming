#!/usr/bin/python3
"""
The "0-add_integer" module.
The module contains one function "add_integer"
Returns the addition of a and b
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    x = [float("inf"), float("-inf")]

    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if a in x or a != a:
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    if b in x or b != b:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
