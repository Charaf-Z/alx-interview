#!/usr/bin/python3
"""Pascal's Triangle."""


def generate_next_row(prev_row):
    """Generate the next row of Pascal's triangle based on the previous row."""
    return (
        [1]
        + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)]
        + [1]
    )


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        triangle.append(generate_next_row(triangle[-1]))
    return triangle
