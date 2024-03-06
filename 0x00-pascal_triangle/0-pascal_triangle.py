#!/usr/bin/python3
"""
A function `def pascal_triangle(n):` that returns a list of lists
of integers representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """ A pascal triangle creation function. """
    pas_triangle = []

    if n <= 0:
        return pas_triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = pas_triangle[i - 1][j - 1] + pas_triangle[i - 1][j]
        pas_triangle.append(row)

    return pas_triangle
