#!/usr/bin/python3
""" The "6-load_from_json_file" Module
"""


import json


def load_from_json_file(filename):
    """ Creates an Object from a “JSON file”
    """
    with open(filename) as f:
        return json.load(f)
