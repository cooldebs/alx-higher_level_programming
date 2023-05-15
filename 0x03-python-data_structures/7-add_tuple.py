#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_b) < 2:
        list_1 = list(tuple_b)
        list_1.append(0)
        tuple_b = tuple(list_1)
    while len(tuple_b) > 2:
        list_1 = list(tuple_b)
        list_1.pop(len(tuple_b) - 1)
        tuple_b = tuple(list_1)

    while len(tuple_a) < 2:
        list_1 = list(tuple_a)
        list_1.append(0)
        tuple_a = tuple(list_1)
    while len(tuple_a) > 2:
        list_1 = list(tuple_a)
        list_1.pop(len(tuple_a) - 1)
        tuple_a = tuple(list_1)
    return tuple([x + y for x, y in zip(list(tuple_a), list(tuple_b))])
