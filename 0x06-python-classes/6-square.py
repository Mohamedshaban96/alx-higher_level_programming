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

    def __init__(self, size=0, position=(0, 0)):
        """setting inistant attributes"""

        self.__size = size
        self.__position = position

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

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or type(value[0]) is not int or \
           type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError "position must be a tuple of 2 positive integers"

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            n = 0
            while n < self.__size:
                print(" " * self.__position[0] + "#" * self.__size)
                n = n + 1
