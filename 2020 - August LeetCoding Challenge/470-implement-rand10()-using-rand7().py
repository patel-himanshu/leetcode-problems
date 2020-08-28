# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3439/

"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10
which generates a uniform random integer in the range 1 to 10.
Do NOT use system's Math.random().

Example 1:
    Input: 1
    Output: [7]

Example 2:
    Input: 2
    Output: [8,4]

Example 3:
    Input: 3
    Output: [8,1,10]

Note:
    (1) rand7 is predefined.
    (2) Each testcase has one argument: n, the number of times that rand10 is called.

Follow up:
    (1) What is the expected value for the number of calls to rand7() function?
    (2) Could you minimize the number of calls to rand7()?
"""

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        parity_num = rand7()
        while parity_num == 7:
            parity_num = rand7()
        
        num_lt_6 = rand7()
        while num_lt_6 > 5:
            num_lt_6 = rand7()
            
        parity = parity_num % 2
        return num_lt_6 + parity*5