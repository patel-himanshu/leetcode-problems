# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3384/

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
        [
        [-1, 0, 1],
        [-1, -1, 2]
        ]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(ans)