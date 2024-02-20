#!/usr/bin/python3
"""This is a class inheritance of Base class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class that inherits the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """return the width of rectangle"""
        return self.__width

    @property
    def heihgt(self):
        """return the height of rectangle"""
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
