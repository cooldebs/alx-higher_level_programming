#!/usr/bin/python3
""" The "2-append_write" Module
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
