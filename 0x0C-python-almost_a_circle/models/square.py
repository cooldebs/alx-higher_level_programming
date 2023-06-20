#!/usr/bin/python3
""" Defines a Square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the Square class inherited
    from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the Square class
        Args:
        width(int): The width of the new Square
        height(int): The height of the new Square
        id(int): The id of the new Square
        x(int): The x coordinate
        y(int): The y coordinate
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints a user-friendly string"""
        return ("[Square] ({}) {}/{} - {}".format(
                 self.id, self.x, self.y, self.height))

    @property
    def size(self):
        """ Gets the size """
        return self.height

    @size.setter
    def size(self, value):
        """ Sets the size """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns argument to each attribute """
        index = 0
        if args is not None and len(args) != 0:
            for argument in args:
                index += 1
                if index == 1:
                    self.id = argument
                if index == 2:
                    self.size = argument
                if index == 3:
                    self.x = argument
                if index == 4:
                    self.y = argument
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """ returns the dictionary representation
        of a Square """
        dictionary = {}
        for index in ["id", "size", "x", "y"]:
            dictionary[index] = getattr(self, index)
        return (dictionary)
