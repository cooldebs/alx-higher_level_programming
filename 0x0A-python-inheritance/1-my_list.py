#!/usr/bin/python3
"""The "1-my_list.py" module"""


class MyList(list):
    """Represents MyList class"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list in ascending sort"""
        print(sorted(self))
