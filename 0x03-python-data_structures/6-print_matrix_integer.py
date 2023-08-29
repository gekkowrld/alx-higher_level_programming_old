#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[1])):
            print("{:d}".format(matrix[i][j]), end="")
            if (j + 1) < len(matrix[1]):
                print(" ", end="")
        print()
