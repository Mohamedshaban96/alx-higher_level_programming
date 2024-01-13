#!/usr/bin/python3
"""This module contains a class that defines a square.
In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
area method returns the area of the square.
"""


class Square:
    """a square class"""

    def __init__(self, size=0):
        """setting inistant attributes"""

    self.__size = size

    def area(self):
        """function return the area of the square"""

        return self.__size * self.__size

    @property
    def size(self):
        """method that return the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """method to set up the size of the square"""

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
