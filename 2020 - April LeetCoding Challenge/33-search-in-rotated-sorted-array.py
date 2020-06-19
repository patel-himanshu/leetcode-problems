# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: 
            return -1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            
            # Check for left rotation
            if nums[mid] >= nums[low]:
                # List in given range is sorted in ascending order
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            # Check for right rotation
            else:
                # List in given range is sorted in ascending order
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        # Element not found
        return -1