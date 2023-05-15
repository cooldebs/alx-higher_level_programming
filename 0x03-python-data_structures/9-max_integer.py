#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    biggest_integer = my_list[0]
    for y in my_list:
        if y > biggest_integer:
            biggest_integer = y
    return (biggest_integer)
