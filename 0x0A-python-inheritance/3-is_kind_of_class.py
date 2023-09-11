#!/usr/bin/python3

"""
Check if the object is remotely
    related to a class
If the object is then return True
"""


def is_kind_of_class(obj, a_class):
    """Check is it is a class or inherits from one

    obj : object
        An object to be checked if it is an instance of
            or inherits from a class

    a_class : class
        The class in which the object will be checked against
    """

    return isinstance(obj, a_class)
