#!/usr/bin/python3

"""
Print the list in an ordered list
All the elements should int
"""


class MyList(list):
    """Inherit from base class 'list`"""

    def print_sorted(self):
        """Print sorted list"""
        print("{}".format(sorted(self)))
