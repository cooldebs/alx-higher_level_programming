#!/usr/bin/python3
"""Defines a Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle class
    Inherits from the BaseGeometry class
    """
    def __init__(self, width, height):
        """Initializes a Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
