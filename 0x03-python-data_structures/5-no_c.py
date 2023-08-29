#!/usr/bin/python3

def no_c(my_string):
    new_str = my_string[:]
    n_s = ''
    for i in range(0, len(new_str)):
        if new_str[i] == 'c' or new_str[i] == 'C':
            continue
        n_s += new_str[i]
    return n_s
