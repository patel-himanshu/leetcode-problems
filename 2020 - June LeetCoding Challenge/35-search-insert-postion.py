# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/

"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

Example 3:
    Input: [1,3,5,6], 7
    Output: 4

Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        i = 0
        while i<len(nums) and nums[i]<target:
            i += 1
        return i