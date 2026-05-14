#!/usr/bin/python3
string = ""
print("{}".format([(string := string + chr(x)) for x in range(ord('A'), ord('Z') + 1)][-1]))
