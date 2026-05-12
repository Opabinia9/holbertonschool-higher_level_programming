#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0] if my_list else None
    for i in my_list:
        max = i if i > max else max
    return (max)
