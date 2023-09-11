#!/usr/bin/python3

"""
Check if a value inherits from
"""


def inherits_from(obj, a_class):
    """Check for inheritance

    obj : object
        An object that will be evaluated

    a_class : class
        A class in which the evaluation will be done against
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True

    return False
