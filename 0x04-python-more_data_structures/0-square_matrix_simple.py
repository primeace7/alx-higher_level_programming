#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    if len(matrix) == 0:
        return matrix
    result = [[x ** 2 for x in row] for row in matrix]
    return result
