# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3421/

"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
    Input: 3
    Output: [1,3,3,1]

Follow up: Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        
        prevRow = [1,1]
        
        for row in range(1, rowIndex):
            newRow = [1] * (row+2)            
            for i in range(row):
                newRow[i+1] = prevRow[i] + prevRow[i+1]
            prevRow = newRow

        return newRow