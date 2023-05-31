#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents the square class"""
    def __init__(self, size=0):
        """Initializes the square object
        Args:
        size(int): size of the square
        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """int: Sets the size attribute
        Returns: __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value(int): size of the square.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square
        Returns: area of the square
        """
        return self.__size ** 2

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __ge__(self, other):
        return self.size >= other.size
