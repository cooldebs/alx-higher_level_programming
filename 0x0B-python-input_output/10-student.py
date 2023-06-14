#!/usr/bin/python3
""" The "10-student" Module
"""


class Student:
    """ Defines a Student class """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        a_dict = {}
        for i in attrs:
            try:
                a_dict[i] = self.__dict__[i]
            except Exception:
                pass
        return a_dict
