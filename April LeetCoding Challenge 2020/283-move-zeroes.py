# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    (1) You must do this in-place without making a copy of the array.
    (2) Minimize the total number of operations.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index, count = 0,0
        while count<len(nums):
            count += 1
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1