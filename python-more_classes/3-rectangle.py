#!/usr/bin/python3
'''An Rectangle Class will be here'''


class Rectangle:
    '''A Rectangle Class'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        width = self.width
        height = self.height
        return 0 if 0 in (width, height) else 2 * (width + height)

    def __str__(self):
        if 0 in (self.width, self.height):
            return ''
        else:
            return ((('#' * self.width) + '\n') * self.height)[:-1]
