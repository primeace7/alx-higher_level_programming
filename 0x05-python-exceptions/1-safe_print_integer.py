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
    except:
        return False



value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
