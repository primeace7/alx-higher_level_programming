#!/usr/bin/python3

'''
safe_print_list - print x elements of a list

Args:
     my_list: the list to print from

     x: the number of elements to print from my_list

Return: The number of elements printed
'''


def safe_print_list(my_list=[], x=0):
    if x < 0:
        raise ValueError('x must be >= 0')
    i = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
        except IndexError:
            print()
            return i
    if i != 0:
        print()
    return i + 1
