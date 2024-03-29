#!/usr/bin/python3

'''
safe_print_list_integers(my_list=[], x=0) - print the first
x elements of a list that are integers

Args:
    my_list: the list to print from

    x: the number of elements to print from my_list
'''


def safe_print_list_integers(my_list=[], x=0):
    if x < 0:
        raise ValueError("x must be >= 0")
    j, i = 0, 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            j += 1
        except ValueError:
            continue

    if j != 0:
        print()
    return j
