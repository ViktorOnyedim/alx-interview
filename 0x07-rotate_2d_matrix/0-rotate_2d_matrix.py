#!/usr/bin/python3
"""
Rotate 2D Matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): List of lists representing the 2D matrix.
    """
    n = len(matrix)

    # Transpose the matrix (swapping rows with columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
