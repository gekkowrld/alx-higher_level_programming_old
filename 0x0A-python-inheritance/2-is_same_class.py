#!/usr/bin/python3

"""
Return True is an object is an instance of
    a class else return False
"""


def is_same_class(obj, a_class):
    """Is the object an instance of a class

    obj : object
        An object to be checked

    a_class: class
        The class in  which the object is to be
            checked against
    """
    if type(obj) is a_class:
        return True
    return False
