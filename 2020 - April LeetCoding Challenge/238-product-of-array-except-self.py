# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/

"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is 
equal to the product of all the elements of nums except nums[i].

Example:
    Input:  [1,2,3,4]
    Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
(including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        L, R, ans = [1]*size, [1]*size, [1]*size
        
        for l in range(1,size):
            L[l] = nums[l-1]*L[l-1]
            
        for r in range(size-2,-1,-1):
            R[r] = nums[r+1]*R[r+1]
        
        for i in range(size):
            ans[i] = L[i]*R[i]
        
        return ans