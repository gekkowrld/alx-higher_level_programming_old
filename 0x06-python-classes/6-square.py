#!/usr/bin/python3

"""Create an empty class that does nothing"""


class Square:
    """Class Square

    This class deals with squares
    """
    def __init__(self, size=0, position=(0, 0)):
        """Create the square attributes

        Args:
          size (int): The size of the square to be created
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get the position details"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Get and or set the position details"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the value of the area of the square

        Since a square is the, well multiplication of two numbers, then
          we multiply the two
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Print '#' to the stdout
        Print the square where size is more than 0, else
            print an empty line
        """
        if self.__size == 0:
            print()
            return
        else:
            [print() for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(' ', end="") for j in range(0, self.__position[0])]
                [print('#', end="") for k in range(0, self.__size)]
                print()
