#!/usr/bin/python

def safe_print_list(my_list=[], x=0):
    i = 0

    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
    except (OSError, OverflowError, IndexError):
        pass
    finally:
        print()
        return i
