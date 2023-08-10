#!/usr/bin/python3

place_holder = ''


def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            place_holder = chr(ord(i) - 32)
        else:
            place_holder = i
        print("{}".format(place_holder), end='')
    print()
