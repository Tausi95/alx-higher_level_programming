#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Compute the square of each integer in the input matrix.
    Returns a new matrix with squared values.
    """
    # Create a new matrix with the same size as the input matrix
    result = [[val ** 2 for val in row] for row in matrix]

    return result

