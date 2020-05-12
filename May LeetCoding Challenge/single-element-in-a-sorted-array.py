# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res