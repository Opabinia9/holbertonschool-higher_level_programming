#!/usr/bin/python3
"""Module: pascal_triangle."""


def pascal_triangle(n: int) -> list:
    """pascal_triangle.

    Returns:
        list of lists or ints, [[1]]

    """
    pt = [[y for y in range(n) if y < x + 1] for x in range(n)]
    for i in range(len(pt)):
        for j in range(len(pt[i])):
            val = 1
            if i > 0 and j > 0 and j < i:
                val = pt[i - 1][j] + pt[i - 1][j - 1]
            pt[i][j] = val

    return pt
