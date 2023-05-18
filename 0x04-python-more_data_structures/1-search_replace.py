#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_lst = [replace if n == search else n for n in my_list]
    return (my_new_lst)
