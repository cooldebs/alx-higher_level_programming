#!/usr/bin/python3
"""Defines a Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square class"""
    def __init__(self, size):
        """Instantiates a Square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of a Square"""
        return self.__size ** 2

    def __str__(self):
        """prints a user-friendly string"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
