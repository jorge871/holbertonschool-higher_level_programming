#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    __size = 0

    def __init__(self, size=0):
        """Init with size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area
