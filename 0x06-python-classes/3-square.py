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

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Return the value of the area of the square

        Since a square is the, well multiplication of two numbers, then
          we multiply the two
        """
        return (self.__size * self.__size)
