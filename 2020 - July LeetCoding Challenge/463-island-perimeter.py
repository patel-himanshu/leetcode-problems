# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3383/

"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

Example:
    Input:
        [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
    Output: 16
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        p = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    if row == 0 or grid[row-1][col] == 0:
                        p += 1
                    if col == 0 or grid[row][col-1] == 0:
                        p += 1
                    if row == ROWS-1 or grid[row+1][col] == 0:
                        p += 1
                    if col == COLS-1 or grid[row][col+1] == 0:
                        p += 1
        return p