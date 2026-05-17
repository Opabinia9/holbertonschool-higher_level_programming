#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        mx = max(a_dictionary.values())
        key = [key for key, value in a_dictionary.items() if value == mx]
        return key[0]
