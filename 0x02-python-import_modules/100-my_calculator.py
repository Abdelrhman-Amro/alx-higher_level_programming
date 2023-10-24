#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit
    import calculator_1

    nargs = len(argv)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if nargs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    print("{} {} {} = ".format(a, op, b), end="")

    if op == '+':
        print(calculator_1.add(a, b))
    elif op == '-':
        print(calculator_1.sub(a, b))
    elif op == '*':
        print(calculator_1.mul(a, b))
    elif op == '/':
        print(calculator_1.div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
