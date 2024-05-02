#!/usr/bin/python3
"""Solution for LockedBoxes."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list): A list of lists representing locked boxes,
            where each box may contain keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or type(boxes) is not list:
        return False
    keys = [0]
    for key in keys:
        for item in boxes[key]:
            if item not in keys and item < len(boxes):
                keys.append(item)
    if len(keys) == len(boxes):
        return True
    return False
