#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    args_len = (len(argv) - 1)
    operators = {'+': add, '-': sub, '*': mul, '/': div}

    if args_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])

    for op in operators:
        if sign == op:
            result = operators[op](a, b)
            print("{} {} {} = {}".format(a, sign, b, result))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
