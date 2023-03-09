#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print(f'Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    ops = ['+', '-', '*', '/']
    if argv[2] not in ops:
        print(f'Unknown operator. Available operators: +, -, * and /')
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])

    print(f'{num1} {argv[2]} {num2} = ', end='', sep='')
    if argv[2] == ops[0]:
        print(f'{add(num1, num2)}')
    elif argv[2] == ops[1]:
        print(f'{sub(num1, num2)}')
    elif argv[2] == ops[2]:
        print(f'{mul(num1, num2)}')
    elif argv[2] == ops[3]:
        print(f'{div(num1, num2)}')
