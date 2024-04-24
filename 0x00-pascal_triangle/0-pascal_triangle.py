"""Pascal Triangle."""


def generate_next_row(prev_row: list[int]) -> list[int]:
    """
    Generate the next row of Pascal's triangle based on the previous row.

    Args:
        prev_row (list[int]): The previous row of Pascal's triangle.

    Return:
        list[int]: The next row of Pascal's triangle.
    """
    return (
        [1]
        + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)]
        + [1]
    )


def pascal_triangle(n: int) -> list[list[int]]:
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Return:
        list[list[int]]: A list of lists representing Pascal's
            triangle up to the nth row.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        triangle.append(generate_next_row(triangle[-1]))
    return triangle
