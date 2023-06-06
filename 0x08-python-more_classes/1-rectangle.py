#!/usr/bin/python3
"""Defines a Rectangle."""


class Rectangle:
    """"Represents a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
        width(int) - represents the width of the rectangle
        height(int) - represents the height of the rectangle

        Raises:
        TypeError: when the value is not an integer
        ValueError: when the value is less than zero

        Returns: None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width attribute
        Returns: __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height attribute
        Returns: __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
