#!/usr/bin/python3
'''
this module contains a function that divides a matrix by a constant
'''


def matrix_divided(matrix, div):
    '''
    Divide a square matrix by a constant

    Args:
    matrix(list): a square matrix in the form of a list of lists
    div(int, float): a constant to divide the matrix with

    Returns(list): a square matrix as a list of lists

    Raises:
    TypeError: matrix isn't a list of list of ints or floats, or each row
        isn't of the same size, or div isn't a number
    ZeroDivisionError: division by zero (div is zero)
    '''

    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
    for row in matrix:
        if type(row) != list:
            raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(elem/div, 2) for elem in row] for row in matrix]
