#!/usr/bin/python3

'''
safe_print_list - print x elements of a list

Args:
     my_list: the list to print from

     x: the number of elements to print from my_list

Return: The number of elements printed
'''


def safe_print_list(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            if j < x:
                print(my_list[j], end='')
                j += 1
        except IndexError:
            print()
            return j
    if j != 0:
        print()
    return j
