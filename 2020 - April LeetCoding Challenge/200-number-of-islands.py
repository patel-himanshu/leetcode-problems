# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3302/

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
    Input:
        11110
        11010
        11000
        00000
    Output: 1

Example 2:
    Input:
        11000
        11000
        00100
        00011
    Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        self.m = len(grid)
        self.n = len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < self.m and 0 <= j < self.n and grid[i][j] == '1':
                grid[i][j] = '0'
                neighbours = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                for n in neighbours:
                    dfs(n[0], n[1])
                return 1
            return 0
               
        return sum(dfs(i,j) for i in range(self.m) for j in range(self.n))