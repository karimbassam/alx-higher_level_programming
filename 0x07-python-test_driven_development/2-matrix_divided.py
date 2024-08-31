#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    matrix: A list of lists of integers or floats.
    div: A number (integer or float) by which to divide the matrix elements.

    Returns:
    A new matrix with each element divided by div, rounded to 2 decimal places.

    Raises:
    TypeError:If matrix is not list of lists of integers/floats if each row of
               the matrix is not the same size or if div is not a number
    ZeroDivisionError: If div is equal to 0.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list)):
        for row in matrix:
            raise TypeError("matrix must be matrix(li of li) of ints/floats")

    if not all(isinstance(elem, (int, float))):
        for row in matrix for elem in row:
            raise TypeError("matrix must be matrix (li of li) of ints/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
