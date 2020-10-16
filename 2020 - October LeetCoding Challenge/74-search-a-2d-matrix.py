# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3497/

"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
    (1) Integers in each row are sorted from left to right.
    (2) The first integer of each row is greater than the last integer of the previous row.

Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
    Output: false

Example 3:
    Input: matrix = [], target = 0
    Output: false

Constraints:
    (1) m == matrix.length
    (2) n == matrix[i].length
    (3) 0 <= m, n <= 100
    (4) -10^4 <= matrix[i][j], target <= 10^4
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return None
        
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False