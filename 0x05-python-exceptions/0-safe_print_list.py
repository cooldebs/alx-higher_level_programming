#!/usr/bin/python3
""" Write a function that prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print()
        return (count)
    except IndexError:
        print()
        return (count)
