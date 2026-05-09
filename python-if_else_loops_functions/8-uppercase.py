#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord('a') <= ord(c) <= ord('z')):
            c = "{}".format(chr(ord(c) + (ord('A') - ord('a'))))
        print(c, end="")
    print()
