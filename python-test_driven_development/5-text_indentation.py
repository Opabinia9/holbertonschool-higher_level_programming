#!/usr/bin/python3
'''a module containing one function'''


def text_indentation(text):
    '''print text newlined on a set of charater, non-removing'''
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        i = 0
        while i < len(text):
            print(text[i], end="")
            if text[i] in ('.', '?', ':'):
                print('\n')
                i += 1
                while i < len(text) and text[i] == ' ':
                    i += 1
                continue
            i += 1
