# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3303/

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
    Input: [
            [1,3,1],
            [1,5,1],
            [4,2,1] ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        for i in range(1,rows):
            grid[i][0] += grid[i-1][0]
        for j in range(1,cols):
            grid[0][j] += grid[0][j-1]
        for r in range(1,rows):
            for c in range(1,cols):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        return grid[-1][-1]