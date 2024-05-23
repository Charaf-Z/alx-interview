#!/usr/bin/python3
"""UTF-8 encoding validator."""


def validUTF8(data):
    """
    Check if a list of integers represents a valid UTF-8 encoding.

    UTF-8 encoding rules:
    - For a single-byte character (0xxxxxxx), the first bit is a 0.
    - For a multi-byte character, it starts with one
        or more 1s followed by a 0 (110xxxxx, 1110xxxx, 11110xxx).
    - Following bytes in a multi-byte character are of the form 10xxxxxx.

    Args:
        data (list of int): A list of integers,
            where each integer represents a byte (0 to 255).

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    nbr_b = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for nbr in data:
        mask_b = 1 << 7
        if nbr_b == 0:
            while mask_b & nbr:
                nbr_b += 1
                mask_b >>= 1
            if nbr_b == 0:
                continue
            if nbr_b == 1 or nbr_b > 4:
                return False
        else:
            if not (nbr & mask_1 and not (nbr & mask_2)):
                return False
        nbr_b -= 1
    if nbr_b == 0:
        return True
    return False
