#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        y = 0
        my_list_mod = my_list.copy()
        for i in my_list:
            if y == idx:
                my_list_mod[idx] = element
                return (my_list_mod)
            y += 1
