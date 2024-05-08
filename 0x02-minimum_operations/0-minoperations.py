#!/usr/bin/python3
"""Provides a function to calculate fewest operations for n 'H' characters."""


def minOperations(n):
    """
    Calculate fewest operations needed for n 'H' characters in a file.

    Args:
        n (int): Target number of 'H' characters.

    Returns:
        int: Fewest operations required for n 'H' characters.
            If impossible, returns 0.
    """
    if n < 2:
        return 0
    ops, cur = 0, 2
    while cur**2 <= n:
        if n % cur == 0:
            ops += cur
            n //= cur
        else:
            cur += 1
    return ops + n * (n > 1)
