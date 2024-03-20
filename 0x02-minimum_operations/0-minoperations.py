#!/usr/bin/env python3
""" Interview Question: Minimum Operations """


def minOperations(n):
    """
    A function that takes one argument as integer to calculate
    minimum operations to reach the n H characters!

    Args:
        n (int): The target number of characters.

    Returns:
        int: The fewest number of operations needed.
        If n is impossible to achieve, return 0.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n >= 2:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
