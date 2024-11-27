#!/usr/bin/python3
"""Change Comes from Within"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            num_coins = total // coin
            count += num_coins
            total -= num_coins * coin

    return count if total == 0 else -1
