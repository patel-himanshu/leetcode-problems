# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3401/

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element. The array may contain duplicates.

Example 1:
    Input: [1,3,5]
    Output: 1

Example 2:
    Input: [2,2,2,0,1]
    Output: 0

Note:
    (1) This is a follow up problem to Find Minimum in Rotated Sorted Array.
    (2) Would allow duplicates affect the run-time complexity? How and why?
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r)//2
            
            if nums[mid] == nums[r]:
                if nums[l] == nums[mid]:
                    l += 1
                elif nums[l] < nums[mid]:
                    r = mid - 1
                else:
                    r = mid
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]