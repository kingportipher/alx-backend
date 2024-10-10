#!/usr/bin/python3
"""
Returns the perimeter of the island described in grid.
"""
def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with adding 4 sides of the square
                perimeter += 4

                # If there is land above the current cell, subtract 2 from the perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # If there is land to the left of the current cell, subtract 2 from the perimeter
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
