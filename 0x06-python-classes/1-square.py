#!/usr/bin/python3

"""Create an empty class that does nothing"""


class Square:
    """Class Square

    This class deals with squares
    """
    def __init__(self, size):
        """Create the square attributes

        Args:
          size (int): The size of the square to be created
        """
        self.__size = size
