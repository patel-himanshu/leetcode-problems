# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
    Input:nums = [1,1,1], k = 2
    Output: 2

Constraints:
    (1) The length of the array is in range [1, 20,000].
    (2) The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curr_sum = 0
        sums = defaultdict(lambda: 0)
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum == k:
                ans += 1
            if curr_sum-k in sums:
                ans += sums[curr_sum - k]
            
            sums[curr_sum] += 1
            
        return ans
