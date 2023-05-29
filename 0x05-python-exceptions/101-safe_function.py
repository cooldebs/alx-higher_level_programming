#!/usr/bin/python3
""" a function that executes a function safely."""
import sys


def safe_function(fct, *args):
    try:
        answer = fct(*args)
        return (answer)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
