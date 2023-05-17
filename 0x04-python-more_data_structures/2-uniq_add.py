#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_integers = []
    total_num = 0
    for i in my_list:
        if i not in uniq_integers:
            uniq_integers.append(i)
            total_num += i
    return (total_num)
