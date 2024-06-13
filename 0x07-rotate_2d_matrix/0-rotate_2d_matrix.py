#!/usr/bin/python3
"""Rotate 90deg a 2D matrix."""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n matrix to be rotated.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # Left to top
            matrix[first][i] = matrix[last - offset][first]
            # Bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            # Right to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Top to right
            matrix[i][last] = top
