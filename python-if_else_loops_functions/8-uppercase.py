#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord('a') <= ord(c) <= ord('z')):
            print(f"{chr(ord(c) + (ord('A') - ord('a')))}", end="")
        else:
            print(c, end="")
    print()
