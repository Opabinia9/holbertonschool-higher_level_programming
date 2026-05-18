#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    count = 0
    while y < x:
        try:
            print("{:d}".format(my_list[y]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
        finally:
            y += 1
    print()
    return count
