# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3496/

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
Follow up:
    (1) Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    (2) Could you do it in-place with O(1) extra space?

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:rotate 1 steps to the right: [7,1,2,3,4,5,6]
                rotate 2 steps to the right: [6,7,1,2,3,4,5]
                rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation:rotate 1 steps to the right: [99,-1,-100,3]
                rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
    (1) 1 <= nums.length <= 2 * 10^4
    (2) -2^31 <= nums[i] <= 2%31 - 1
    (3) 0 <= k <= 10^5
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        # for i in range(k):
        #     nums.insert(0, nums.pop())

        nums[:] = nums[-k:] + nums[:-k]