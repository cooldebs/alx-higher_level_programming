#!/usr/bin/python3
"""Defines a LockedClass class"""


class LockedClass:
    """Locked class to prevent creation of new instances"""
    __slots__ = ['first_name']
    pass
