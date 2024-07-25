#!/usr/bin/python3
""" A file with function to make Change comes from within
"""


def makeChange(coins, total):
    """ A pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the fewest number of coins needed
    # for each total from 0 to 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array starting from the value of the current coin
        for amount in range(coin, total + 1):
            # Update dp[amount] only if current coin can contribute
            # to a better solution
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] remains infinity, it means the total cannot be met
    # by any combination of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
