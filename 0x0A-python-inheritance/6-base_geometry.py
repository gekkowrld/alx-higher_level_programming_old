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
