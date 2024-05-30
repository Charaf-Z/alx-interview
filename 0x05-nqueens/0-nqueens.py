#!/usr/bin/python3
"""N Queens module helper."""

import sys


def validate_args():
    """Validate the given argument."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    nbr = int(sys.argv[1])

    if nbr < 4:
        print("N must be at least 4")
        exit(1)

    return nbr


def queens(n, row=0, columns=[], diag1=[], diag2=[]):
    """Generate all valid queen position."""
    if row == n:
        yield columns
    else:
        for col in range(n):
            if (
                col not in columns
                and (row + col) not in diag1
                and (row - col) not in diag2
            ):
                yield from queens(
                    n,
                    row + 1,
                    columns + [col],
                    diag1 + [row + col],
                    diag2 + [row - col],
                )


def solve(n):
    """Solve the N-Queens problem and print each solution."""
    for solution in queens(n):
        board = [[row, col] for row, col in enumerate(solution)]
        print(board)


if __name__ == "__main__":
    solve(validate_args())
