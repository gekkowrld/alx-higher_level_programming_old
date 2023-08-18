#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for first_list in matrix:
        result.append(list(map(lambda x: x**2, first_list)))

    return result
