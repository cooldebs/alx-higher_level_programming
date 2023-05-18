#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ a function that prints a dictionary by ordered keys """
    for keys in sorted(a_dictionary.keys()):
        print("{}: {}".format(keys, a_dictionary[keys]))
