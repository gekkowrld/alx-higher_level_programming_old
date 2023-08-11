#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args_len = (len(argv) - 1)
    args_name = 'argument' if args_len == 1 else 'arguments'
    args_name += '.' if args_len == 0 else ':'
    print("{} {}".format(args_len, args_name))

    for i in argv:
        if argv.index(i) == 0:
            continue
        print("{}: {}".format(argv.index(i), i))
