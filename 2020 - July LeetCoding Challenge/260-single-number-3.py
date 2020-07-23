# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3399/

"""
Given an array of numbers nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
    Input:  [1,2,1,3,2,5]
    Output: [3,5]

Note:
    (1) The order of the result is not important. So in the above example, [5, 3] is also correct.
    (2) Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = defaultdict(int)
        for i in range(len(nums)):
            if ans[nums[i]] == 1:
                del ans[nums[i]]
            else:
                ans[nums[i]] += 1
        return ans.keys()