# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3312/

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
    Input: 
        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0
    Output: 4
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        
        side = 0
        count_rows, count_cols = len(matrix), len(matrix[0])
        dp = [[0 for col in range(count_cols+1)] for row in range(count_rows+1)]
        
        for row in range(1, count_rows+1):
            for col in range(1, count_cols+1):
                if matrix[row-1][col-1] == '1':
                    dp[row][col] = 1 + min(dp[row-1][col-1], dp[row][col-1], dp[row-1][col])
                side = max(side, dp[row][col])
        
        return side*side