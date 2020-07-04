# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3380/

"""
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
    Input: n = 10
    Output: 12
    Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
    (1) 1 is typically treated as an ugly number.
    (2) n does not exceed 1690.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        count = 1
        a,b,c = 0,0,0
        
        while count < n:
            count += 1
            ugly = min(uglies[a]*2, uglies[b]*3, uglies[c]*5)
            uglies.append(ugly)
            
            """
            Multiple if conditions because at some point, we may any of the following conditions:
            (1) uglies[a]*2 == uglies[b]*3
            (2) uglies[a]*2 == uglies[c]*5
            (3) uglies[b]*3 == uglies[c]*5
            Then we would have to increase 2 variables out of a,b,c    
            """
            if ugly == uglies[a]*2: 
                a += 1
            if ugly == uglies[b]*3:
                b += 1
            if ugly == uglies[c]*5:
                c += 1

        return uglies[-1]