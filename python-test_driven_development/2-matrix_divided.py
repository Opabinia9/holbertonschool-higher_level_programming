#!/usr/bin/python3
'''A module to hold one function'''


def matrix_divided(matrix, div):
    '''divide a matrix by a value'''
    if (
        type(matrix) is not list
        or not all(type(x) is list for x in matrix)
        or not all(type(y) in (int, float) for x in matrix for y in x)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    elif len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(n / div, 2) for n in i] for i in matrix]
