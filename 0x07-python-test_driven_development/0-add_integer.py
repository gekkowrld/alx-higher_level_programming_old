#!/usr/bin/python3

"""
The function add_integer is used to add
integers together

If a variable is not an int, it should be
converted to one.

If it can't, then raise an error
"""

def add_integer(a, b=98):
	"""Add an integer with another integer or float
	
	An example of a number can be 1 and 3 which should be 4

	The function should catch the ValueError and TypeError,
		but only the TypeError should be raised
	"""
	try:
		a = int(a)
	except (TypeError, ValueError, OverflowError):
		raise TypeError("a must be an integer")
	try:
		b = int(b)
	except (TypeError, ValueError, OverflowError):
		raise TypeError("b must be an integer")

	return a + b
