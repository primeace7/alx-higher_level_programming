#!/usr/bin/python3
'''
safe_print_integer - print an integer with "{:d}".format()

Args:
     value: value to be printed

Return: True if value is an integer and was printed, False otherwise
'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
