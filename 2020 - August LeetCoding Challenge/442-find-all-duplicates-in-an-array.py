# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/

"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
    Input: [4,3,2,7,8,2,3,1]
    Output: [2,3]
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                ans.append(abs(n))
            else:
                nums[index] *= -1
        return ans