#!/usr/bin/python3

"""
Read the content of a file
UTF-8 encoding is used when reading the files
The file is assumed to contain text only
"""


def read_file(filename=""):
    """Read a file and print it out to the stdout

        filename : string
            The file to be read from
    """
    with open(filename, "r", encoding="UTF-8") as file:
        print("{}".format(file.read()))
