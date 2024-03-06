#!/usr/bin/python3
"""
A function `def pascal_triangle(n):` that returns a list of lists
of integers representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """ A pascal triangle creation function. """
    pas_triangle = []

    if n <= 0:
        # Return empty triangle
        return pas_triangle

    for i in range(n):
        # for n = 1 or 2 get this [1] &or [1, 1]
        row = [1] * (i + 1)
        # for n > 2, i > 1 means i = 2, 3 ... get this [1, 2, 1] on row3
        if i > 1:
            for j in range(1, i):  # Range must start at 1 like [..., 2,...]
                # row[j] is here [1, row[j], 1] where 2 ones from [1]*(1+1)
                row[j] = pas_triangle[i - 1][j - 1] + pas_triangle[i - 1][j]
        pas_triangle.append(row)

    return pas_triangle
