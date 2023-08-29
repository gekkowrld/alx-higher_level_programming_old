#!/usr/bin/python3

"""Create an empty class that does nothing"""


class Square:
    """Class Square

    This class deals with squares
    """
    def __init__(self, size=0):
        """Create the square attributes

        Args:
          size (int): The size of the square to be created
        """
        self.__size = size

    @property
    def size(self):
        """Get and or set the values of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the value of the area of the square

        Since a square is the, well multiplication of two numbers, then
          we multiply the two
        """
        return (self.__size * self.__size)
