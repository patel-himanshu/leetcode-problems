# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3381/

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note: 0 ≤ x, y < 231.

Example:
    Input: x = 1, y = 4
    Output: 2
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y == 0: return 0

        count = max(len(bin(x)[2:]), len(bin(y)[2:]))
        while x or y:
            # print(count)
            if x&1 == y&1:
                count -= 1
            x = x>>1
            y = y>>1
        return count

        """
        return bin(x^y).count('1')
        """
        