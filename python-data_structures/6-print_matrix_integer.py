#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for n in range(len(i)):
            if n == 0:
                print("{:d}".format(0), end="")
                continue
            print(" {:d}".format(i[n]), end="")
        print()
