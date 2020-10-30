# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3513/

"""
Given an integer array nums, return the number of longest increasing subsequences.

Example 1:
    Input: nums = [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Constraints:
    (1) 0 <= nums.length <= 2000
    (2) -10^6 <= nums[i] <= 10^6
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp_len = [1] * n
        dp_cnt = [1] * n
        
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if dp_len[j] + 1 > dp_len[i]:
                    dp_len[i] = dp_len[j] + 1
                    dp_cnt[i] = dp_cnt[j]
                elif dp_len[j] + 1 == dp_len[i]:
                    dp_cnt[i] += dp_cnt[j]
        
        max_len = max(x for x in dp_len)
        count = 0
        
        for l, c in zip(dp_len, dp_cnt):
            if l == max_len:
                count += c
        
        return count