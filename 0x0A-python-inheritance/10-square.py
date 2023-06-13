#!/usr/bin/python3
"""Defines a Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square class
    Inherits a Rectangle class
    """
    def __init__(self, size):
        """Instantiates a Square class"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of the Square"""
        return self.__size ** 2
