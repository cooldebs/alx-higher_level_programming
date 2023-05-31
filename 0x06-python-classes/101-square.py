#!/usr/bin/python3
"""Define a Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object

        Args:
            size(int) - represents size of the new square.
            position(tuple): The coordinates of the new square.

        Returns: None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Sets the size attribute
        Return: __size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """sets the property of the coordinates of the square.
        Raises:
        TypeError: if value != a tuple of 2 integers < 0
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int)
                and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.
        Return: area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
