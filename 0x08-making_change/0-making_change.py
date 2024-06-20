#!/usr/bin/python3
"""Get the fewest number of coins to meet a given amount."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
        coins (list of int): The values of the coins in your possession.
        total (int): The total amount to achieve with the coins.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins, return -1.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    # Initialize the dp array with the largest value.
    min_coins = [float("inf")] * (total + 1)
    min_coins[0] = 0  # Base case

    for coin in coins:
        for amount in range(coin, total + 1):
            if min_coins[amount - coin] != float("inf"):
                min_coins[amount] = min(
                    min_coins[amount], min_coins[amount - coin] + 1
                )

    return min_coins[total] if min_coins[total] != float("inf") else -1
