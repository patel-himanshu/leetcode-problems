# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3392/

"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
    Input: 2.00000, 10
    Output: 1024.00000

Example 2:
    Input: 2.10000, 3
    Output: 9.26100

Example 3:
    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2^(-2) = 1/2^2 = 1/4 = 0.25

Note:
    (1) -100.0 < x < 100.0
    (2) n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if not n: return 1
            elif n == 1: return x
            elif n & 1:
                return x * helper(x, n-1)
            return helper(x*x, n//2)
        
        if n >= 0:
            return helper(x, n)
        return helper(1/x, -n)