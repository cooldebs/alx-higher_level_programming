#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """
        Initializes a Square
        Args: size(int) - represents the size of a square

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a Square
        Return: Area of a Square
        """
        return self.__size ** 2
