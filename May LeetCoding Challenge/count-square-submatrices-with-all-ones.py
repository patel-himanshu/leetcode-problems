# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336/

"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
    Input: matrix =
        [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
        ]
    Output: 15
    Explanation: 
        There are 10 squares of side 1.
        There are 4 squares of side 2.
        There is  1 square of side 3.
        Total number of squares = 10 + 4 + 1 = 15.

Example 2:
    Input: matrix = 
        [
        [1,0,1],
        [1,1,0],
        [1,1,0]
        ]
    Output: 7
    Explanation: 
        There are 6 squares of side 1.  
        There is 1 square of side 2. 
        Total number of squares = 6 + 1 = 7.

Constraints:
    (1) 1 <= arr.length <= 300
    (2) 1 <= arr[0].length <= 300
    (3) 0 <= arr[i][j] <= 1
"""

class Solution:
    def countSquares(self, matrix): # countSquares(self, matrix: List[List[int]]) -> int
        m = len(matrix)     # Number of rows
        n = len(matrix[0])  # Number of columns
        ans = []

        for i in range(m):
            temp = []
            for j in range(n):
                top = i-1
                left = j-1

                if top >= 0 and left >= 0 and matrix[i][j]:
                    temp.append(1 + min(ans[top][j], temp[left], ans[top][left]))
                else:
                    temp.append(matrix[i][j])
            ans.append(temp)

        return sum([sum(row) for row in ans])

inputs = [
    [
        [0,1,1,1], 
        [1,1,1,1], 
        [0,1,1,1]
    ],
    [
        [1,0,1],
        [1,1,0], 
        [1,1,0] 
    ]
]

outputs = [15, 7]

S = Solution()
for i in inputs:
    print(S.countSquares(i))