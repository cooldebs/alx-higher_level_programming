#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        weight = 0
        for x, y in my_list:
            number += x * y
            weight += y
        if weight == 0:
            return (0)
        return (number / weight)
    return (0)
