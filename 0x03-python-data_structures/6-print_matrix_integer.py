#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in row:
            if number == row[-1]:
                use = ''
            else:
                use = ' '
            print('{:d}'.format(number), end=use)
        print()
