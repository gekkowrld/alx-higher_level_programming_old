#!/usr/bin/python3

"""
A geometry class that holds geometry
    of any description

The baseGeometry class specifies how other geometrical
    shapes acts
"""


class BaseGeometry:
    """ The base class for geometry"""

    def area(self):
        """raise an exception for not being implemented"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate the values passed"""

        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
