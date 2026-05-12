#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    value1, value2 = 0, 0
    if len(tuple_a) >= 1:
        value1 += tuple_a[0]
        if len(tuple_a) >= 2:
            value2 += tuple_a[1]
    if len(tuple_b) >= 1:
        value1 += tuple_b[0]
        if len(tuple_b) >= 2:
            value2 += tuple_b[1]
    new_tuple = (value1, value2)
    return (new_tuple)
