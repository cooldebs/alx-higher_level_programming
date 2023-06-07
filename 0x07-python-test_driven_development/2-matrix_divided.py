#!/usr/bin/python3
"""
The "2-matrix_dividend" module
The module has one function "matrix_dividend"
Returns the division of all elements of a matrix
"""


def matrix_divided(matrix=[0], div="pain"):
    """
    Returns matrix[i][j] / div
    """
    x = [float('inf'), float('-inf')]
    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError(
                    "matrix must be a matrix \
(list of lists) of integers/floats")

    length = len(matrix[0])
    n_matrix = [[]]

    for row in matrix:
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if (type(div) is not int and type(div) is not float) \
       or div in x or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    x = 0
    for rows in matrix:
        for cols in rows:
            n_matrix[x].append(round(cols/div, 2))
        n_matrix.append([])
        x += 1

    n_matrix.pop()
    return (n_matrix)
