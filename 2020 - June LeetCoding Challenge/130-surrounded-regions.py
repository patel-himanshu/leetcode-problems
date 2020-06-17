# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3363/

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
    X X X X
    X O O X
    X X O X
    X O X X

After running your function, the board should be:
    X X X X
    X X X X
    X X X X
    X O X X

Explanation: Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return board
        
        self.m = len(board)
        self.n = len(board[0])
        
        def dfs(i, j):
            if 0<=i<self.m and 0<=j<self.n and board[i][j]=='O':
                board[i][j] = 'C'
                
                neighbours = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                for n in neighbours:
                    dfs(n[0], n[1])
        
        for i in range(self.m):
            dfs(i, 0)
            dfs(i, self.n-1)
        
        for j in range(self.n):
            dfs(0, j)
            dfs(self.m-1, j)
            
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'C':
                    board[i][j] = 'O'
                elif board[i][j ]== 'O':
                    board[i][j] = 'X'