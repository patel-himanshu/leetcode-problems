# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3402/

"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
    Input: 38
    Output: 2 
    Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
                Since 2 has only one digit, return it.

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num-1)%9 if num else 0        