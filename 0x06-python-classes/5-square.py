#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Initializes the Square Object
        Args: size(int) - represents the size of the square
        Return: None

        Raises:
        TypeError: if size if not an integer
        ValueError: if size < 0
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
        Return: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
