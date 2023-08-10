#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_digit(num):
    return num - (10 * int(num/10))

l_digit = last_digit(number)

last_part = ''
if l_digit > 5:
    last_part = 'and is greater than 5'
elif l_digit == 0:
    last_part = 'and is 0'
elif l_digit < 6 and not 0:
    last_part = 'and is less than 6 and not 0'

print("Last digit of {} is {} {}".format(number, l_digit, last_part))
