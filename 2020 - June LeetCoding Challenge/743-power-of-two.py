# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354/

"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
    Input: 1
    Output: true 
    Explanation: 20 = 1

Example 2:
    Input: 16
    Output: true
    Explanation: 24 = 16

Example 3:
    Input: 218
    Output: false
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        flag = True
        while n:
            count += n&1
            n = n>>1
            if count > 1:
                flag = False
                break
        return flag and count
    
        """ 
        ================ Alternate method =====================
        return n>0 and n&(n-1)==0
        """