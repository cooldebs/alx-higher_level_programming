#!/usr/bin/python3
"""Define the Python class MagicClass that does
exactly the same as the following Python bytecode
"""

import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """Initializes a MagicClass
        Args:
        radius (float or int): The radius of the new MagicClass

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area of the MagicClass.
        Return: Area of the MagicClass
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculates the circumference of the MagicClass
        Return: Circumference of the MagicClass
        """
        return (2 * math.pi * self.__radius)
