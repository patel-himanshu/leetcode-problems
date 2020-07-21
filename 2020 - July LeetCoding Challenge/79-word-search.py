# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3397/

"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
    board =
        [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]

    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.

Constraints:
    (1) board and word consists only of lowercase and uppercase English letters.
    (2) 1 <= board.length <= 200
    (3) 1 <= board[i].length <= 200
    (4) 1 <= word.length <= 10^3
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    ans = self.helper(board, rows, cols, row, col, word[1:])
                    if ans: return True
        
        return False
    
    def helper(self, board, rows, cols, i, j, target):
        temp = board[i][j]
        board[i][j] = "*"
        
        if not len(target): return True
        
        for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < rows and 0 <= y < cols and board[x][y] == target[0]:
                check = self.helper(board, rows, cols, x, y, target[1:])
                if check: return True
        
        board[i][j] = temp
        return False