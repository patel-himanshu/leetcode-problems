# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3395/

"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints:
    (1) Each string consists only of '0' or '1' characters.
    (2) 1 <= a.length, b.length <= 10^4
    (3) Each string is either "0" or doesn't contain any leading zero.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = len(a) + 1 if len(a) >= len(b) else len(b) + 1
        a = "0" * (max_len - len(a)) + a
        b = "0" * (max_len - len(b)) + b
        ans = [0] * max_len
        carry = 0
        
        for i in range(-1, -max_len - 1, -1):
            sum_at_i = int(a[i]) + int(b[i]) + carry
            
            if sum_at_i == 0 or sum_at_i == 1:
                ans[i] = str(sum_at_i)
                carry = 0
            elif sum_at_i == 2:
                ans[i] = "0"
                carry = 1
            else:
                ans[i] = "1"
                carrry = 1
                
        return "".join(ans) if ans[0] != "0" else "".join(ans[1:])