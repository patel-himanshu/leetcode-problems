# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3387/

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
    Input: nums = [1,2,3]
    Output:
        [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
        ]
"""

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)+1):
            for element in combinations(nums, i):
                ans.append(list(element))
        return ans

"""
================== ALITER ===================

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        power_set_size = 2**len(nums)
        counter = 0

        while counter < power_set_size:
            temp = []
            for i in range(len(nums)):
                if counter & 1<<i:
                    temp.append(nums[i])
            ans.append(temp)
            counter += 1
            
        return ans
"""