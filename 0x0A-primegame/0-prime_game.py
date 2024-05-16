#!/usr/bin/python3
""" A prime game by take turns choosing a prime number from the set
and removing that number and its multiples from the set.
The player that cannot make a move loses the game.
"""


def isPrime(n):
    """ To check if a number is a prime number
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


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
    maria_wins = 0
    ben_wins = 0
    rd = 0  # rounds game be played
    primes_count = 0

    for rd in range(x):
        if rd >= len(nums):
            print("Game Over!!!")
            break
        n = nums[rd]
        primes_count = sum(1 for i in range(2, n+1) if isPrime(i))
        # If the count of primes is odd, Maria wins; otherwise, Ben wins
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
