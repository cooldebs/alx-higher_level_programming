#!/usr/bin/python3
"""Defines a Rectangle."""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle class
        Args:
        width(int) - represents the width of the rectangle
        height(int) - represents the height of the rectangle

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than zero

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle
        Returns: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle
        Returns: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """return the rectangle with the character #"""
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return (rectangle_str)
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str
