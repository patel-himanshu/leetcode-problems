# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3510/

"""
You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
    (1) "a->b" if a != b
    (2) "a" if a == b

Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
                [0,2] --> "0->2"
                [4,5] --> "4->5"
                [7,7] --> "7"

Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
                [0,0] --> "0"
                [2,4] --> "2->4"
                [6,6] --> "6"
                [8,9] --> "8->9"

Example 3:
    Input: nums = []
    Output: []

Example 4:
    Input: nums = [-1]
    Output: ["-1"]

Example 5:
    Input: nums = [0]
    Output: ["0"]

Constraints:
    (1) 0 <= nums.length <= 20
    (2) -2^31 <= nums[i] <= 2^31 - 1
    (3) All the values of nums are unique.
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        
        d = {}
        ans = []
        
        for num in nums:
            d[num] = 1
        
        i = n-1
        while i >= 0:
            stop = nums[i]
            curr = nums[i]
            while i >= 0 and curr in d:
                curr -= 1
                i -= 1
            start = curr + 1
            if start == stop:
                ans.insert(0, str(start))
            else:
                ans.insert(0, str(start) + "->" + str(stop))
        
        return ans