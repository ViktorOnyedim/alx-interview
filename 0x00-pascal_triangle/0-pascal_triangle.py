#!/usr/bin/python3
"""
Function that returns a list of lists of integers 
representing the Pascal's triangle of n rows
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal's triangle of n
    """


    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            # Set the first and last element in each row to be 1
            if j == 0 or j == i:
                row.append(1)
            else:
                # Sum the two numbers just above the number
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle