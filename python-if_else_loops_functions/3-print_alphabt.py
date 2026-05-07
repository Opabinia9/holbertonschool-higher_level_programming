#!/usr/bin/python3
for letter in range(ord('a'), ord('z')):
    if letter in (ord('q'), ord('e')):
        continue
    print("{}".format(chr(letter)), end="")
