#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a_new_list = []
    for i in my_list:
        if i % 2 == 0:
            a_new_list.append(True)
        else:
            a_new_list.append(False)
    return a_new_list
