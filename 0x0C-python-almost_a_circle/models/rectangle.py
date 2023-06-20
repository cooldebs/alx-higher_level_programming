#!/usr/bin/python3
""" Defines a Rectangle class. """


from models.base import Base


class Rectangle(Base):
    """ Defines a Rectangle class inherited from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
        width (int): The width of the new Rectangle
        height (int): The height of the new Rectangle
        x (int): The x coordinate
        y (int): The y coordinate
        id (int): The id of the new Rectangle

        Raises:
        TypeError: If width or height is not an int.
        ValueError: If width or height <= 0.
        TypeError: If x or y is not an int.
        ValueError: If x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x coordinate """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets the y coordinate """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the y coordinate """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates the area of the rectangle
        Return: area
        """
        return self.width * self.height

    def display(self):
        """  prints in stdout the Rectangle
        instance with the character #
        """
        for h in range(0, self.y):
            print()
        for row in range(0, self.height):
            for pad_x in range(0, self.x):
                print(end=" ")
            for col in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Prints a user-friendly string """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                 self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute
        Args:
        *args (ints): New attribute values.
        - 1st argument represents id attribute
        - 2nd argument represents width attribute
        - 3rd argument represent height attribute
        - 4th argument represents x attribute
        - 5th argument represents y attribute
        **kwargs (dict): New key/value pairs of attributes.
        """
        index = 0
        if args is not None and len(args) != 0:
            for argument in args:
                index += 1
                if index == 1:
                    self.id = argument
                elif index == 2:
                    self.__width = argument
                elif index == 3:
                    self.__height = argument
                elif index == 4:
                    self.__x = argument
                elif index == 5:
                    self.__y = argument
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """ returns the dictionary representation
        of a Rectangle """
        dictionary = {}
        for index in ["id", "width", "height", "x", "y"]:
            dictionary[index] = getattr(self, index)
        return (dictionary)
