#!/usr/bin/python3
""" a function that divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    result, new_list = 0, []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            continue
    return new_list
