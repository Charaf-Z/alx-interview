#!/usr/bin/python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    new_row = [1]
    result = pascal_triangle(n - 1)
    last_row = result[-1]
    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])
    new_row += [1]
    result.append(new_row)
    return result
