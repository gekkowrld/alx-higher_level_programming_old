#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number)
    last_number = number
    while number > 9:
        number = number % 10
        last_number = number

    print(last_number, end='')
    return last_number
