#!/usr/bin/python3
""" The "101-add_attribute" module
"""


def add_attribute(obj, key, value):
    """ adds an attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
