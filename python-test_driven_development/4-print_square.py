#!/usr/bin/python3
'''a module with one function'''


def print_square(size):
    '''print a square'''
    if type(size)  is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print('#' * size)
