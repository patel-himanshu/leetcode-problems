# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:
    Input: num = 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
    Input: num = 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

Constraints:
    (1) The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
    (2) num >= 1
    (3) You could assume no leading zero bit in the integer’s binary representation.
    (4) This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""

class Solution:
    def findComplement(self, num: int) -> int:
        complement = ''
        for i in format(num, 'b'):
            if i=='0':
                complement += '1'
            else:
                complement += '0'
        return int(complement,2)