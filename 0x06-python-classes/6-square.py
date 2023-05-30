#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square Object
        Return: None

        Args:
        size(int) - represents the size of the square
        position(tuple) - represents the coordinates of the square

        Raises:
        TypeError: if type is not an integer
        ValueError: if size is less than zero
        """

        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """Sets the size attribute
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

    @property
    def position(self):
        """Sets the position attribute
        Return: __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int)
                and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a square
        Return: Area of the square
        """
        return self.__size ** 2

    def pos_print(self):
        """returns the position in spaces"""

        pos = ""
        if self.size == 0:
            return "\n"
        for x in range(self.position[1]):
            pos += "\n"
        for x in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
