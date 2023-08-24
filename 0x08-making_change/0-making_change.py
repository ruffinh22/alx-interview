#!/usr/bin/python3
"""
Module for calculating the fewest number of coins needed to meet a given total
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of coin values.
        total (int): Total amount to achieve.

    Returns:
        int: Fewest number of coins needed to meet the total amount.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]

# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

