#!/usr/bin/python3
""" A prime game by take turns choosing a prime number from the set
and removing that number and its multiples from the set.
The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """ A function to choose a prime number from a set
    and removing that number and its multiples.

    Args:
        x: is the number of rounds
        nums: is an array of n

    Returns:
        Name of Player that won the most rounds,
        if the winner cannot be determined, return None,
        n and x will not be larger than 10000.
    """
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    
    # Generate primes using Sieve of Eratosthenes algorithm
    primes = [True] * (max_num + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_num + 1, i):
                primes[j] = False
    
    marias_wins, bens_wins = 0, 0
    
    # Count primes less than n for each round
    for n in nums:
        primes_count = sum(1 for i in range(2, n+1) if primes[i])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
