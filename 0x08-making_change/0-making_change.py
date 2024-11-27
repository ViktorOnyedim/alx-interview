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

    # dp = [float('inf')] * (total + 1)
    # dp[0] = 0

    # for i in range(1, total + 1):
    #     for coin in coins:
    #         if i - coin >= 0:
    #             dp[i] = min(dp[i], dp[i - coin] + 1)

    # return dp[total] if dp[total] != float('inf') else -1

# def makeChange(coins, total):
#     if total <= 0:
#         return 0

#     # Sort coins in descending order for the greedy approach
#     coins.sort(reverse=True)
#     count = 0

#     for coin in coins:
#         if total == 0:
#             break
#         if coin <= total:
#             num_coins = total // coin
#             count += num_coins
#             total -= num_coins * coin

#     return count if total == 0 else -1