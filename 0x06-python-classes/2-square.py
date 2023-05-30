#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents the Square"""
    def __init__(self, size=0):
        """Initializes the Square class
        Args: size(int) - represents the size of the square
        Returns: none
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
