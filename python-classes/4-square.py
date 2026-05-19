#!/usr/bin/python3
'''An empty class with nothing'''


class Square:
    '''an empty class with nothing'''

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
