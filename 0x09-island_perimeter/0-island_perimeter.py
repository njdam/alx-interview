#!/usr/bin/python3
""" A function def island_perimeter(grid): that returns the perimeter
of the island described in grid.
"""


def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume 4 sides initially
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # If upper cell is land, subtract 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # If left cell is land, subtract 2

    return perimeter
