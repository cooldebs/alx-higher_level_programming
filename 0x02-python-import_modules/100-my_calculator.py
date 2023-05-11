#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv, exit

    if len(argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    elif argv[2] == '+':
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     calc.add(int(argv[1]), int(argv[3]))))
    elif argv[2] == '-':
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     calc.sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == '*':
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     calc.mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == '/':
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     calc.div(int(argv[1]), int(argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
