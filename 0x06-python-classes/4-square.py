#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Initializes a square
        Args: size(int) - represents the size of a square
        Return: None

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Gets the size attribute
        Return: __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of a square
        Return: area of a square
        """
        return self.__size ** 2
