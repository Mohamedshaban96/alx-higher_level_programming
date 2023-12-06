#!/usr/bin/python3
"""creating a Square class"""


class Square:
    """a square class """
    def __init__(self, size=0):
        """setting inistant attributes"""
        self.__size = size

        if type(size) is not int:
            raise TypeError ("size must be an integer")
        
        if size < 0:
            raise ValueError ("size must be >= 0")
