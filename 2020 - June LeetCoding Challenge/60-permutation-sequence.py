# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3366/

"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note:
    (1) Given n will be between 1 and 9 inclusive.
    (2) Given k will be between 1 and n! inclusive.

Example 1:
    Input: n = 3, k = 3
    Output: "213"

Example 2:
    Input: n = 4, k = 9
    Output: "2314"
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num-1)
        
        k -= 1
        ans = []
        fact = factorial(n-1)
        nums = list(range(1, n+1))
        
        for i in range(n-1, 0, -1):
            index = k // fact
            ans.append(str(nums.pop(index)))
            k %= fact
            fact //= i
        
        return ''.join(ans) + str(nums[0])