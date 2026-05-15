#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print(f"{k}: {v}") for k, v in sorted(list(a_dictionary.items()))]
