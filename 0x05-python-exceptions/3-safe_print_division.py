#!/usr/bin/python3
""" a function that divides 2 integers and prints the result."""


def safe_print_division(a, b):
    dividend = 0
    try:
        dividend += a / b
    except ZeroDivisionError:
        dividend = None
    except TypeError:
        dividend = None
    finally:
        print("Inside result: {}".format(dividend))
        return (dividend)
