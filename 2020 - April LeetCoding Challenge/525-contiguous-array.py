# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/

"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000. 
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        new_nums = [-1 if i==0 else i for i in nums]
        total = 0
        cum_sum = [0]*len(new_nums)
        indices = {}
        max_len = 0

        for i in range(len(new_nums)):
            total += new_nums[i]
            cum_sum[i] = total

            if total == 0:
                max_len = i+1

            if total not in indices.keys():
                indices[total] = [i,i]
            else:
                indices[total][1] = i
        
        for j in indices:
            max_len = max(max_len, indices[j][1] - indices[j][0])
        
        return max_len