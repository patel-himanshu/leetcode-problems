# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/

"""
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check 
 whether this string is valid. We define the validity of a string by these rules:
    
    (1) Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    (2) Any right parenthesis ')' must have a corresponding left parenthesis '('.
    (3) Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    (4) '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    (5) An empty string is also valid.

Example 1:
    Input: "()"
    Output: True

Example 2:
    Input: "(*)"
    Output: True

Example 3:
    Input: "(*))"
    Output: True

Note: The string size will be in the range [1, 100].
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        bmax, bmin = 0, 0
        for i in s:
            if i == '(':
                bmax += 1
                bmin += 1
            elif i == ')':
                bmax -= 1
                bmin = max(bmin-1, 0)
            else:
                bmax += 1
                bmin = max(bmin-1, 0)
            
            if bmax < 0:
                return False
        
        return bmin == 0