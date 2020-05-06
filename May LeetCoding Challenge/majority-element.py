# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums)//2
        nums_unique = set(nums)
        for i in nums_unique:
            if nums.count(i) > limit:
                return i