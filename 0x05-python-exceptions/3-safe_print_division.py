#!/usr/bin/python3

'''
safe_print_division - divide two integers and print the result

Args:
    a: the dividend

    b: the divisor

Return: the quotient, or None if there was an error

'''

def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
        raise
    finally:
        print('Inside result: {}'.format(result))
        return result


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
