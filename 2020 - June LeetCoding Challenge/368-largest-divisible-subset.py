# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3359/

"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
    Input: [1,2,3]
    Output: [1,2] (of course, [1,3] will also be ok)

Example 2:
    Input: [1,2,4,8]
    Output: [1,2,4,8]
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(size):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j])+1:
                    dp[i] = dp[i] + [nums[j]]
        
        return max(dp, key=len)