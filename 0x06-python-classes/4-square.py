#!/usr/bin/python3
"""creating a Square class
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
