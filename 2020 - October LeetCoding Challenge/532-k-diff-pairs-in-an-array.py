# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3482/

"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
    (1) 0 <= i, j < nums.length
    (2) i != j
    (3) a <= b
    (4) b - a == k 

Example 1:
    Input: nums = [3,1,4,1,5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
    Input: nums = [1,2,3,4,5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
    Input: nums = [1,3,1,5,4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Example 4:
    Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
    Output: 2

Example 5:
    Input: nums = [-1,-2,-3], k = 1
    Output: 2
 
Constraints:
    (1) 1 <= nums.length <= 104
    (2) -107 <= nums[i] <= 107
    (3) 0 <= k <= 107
"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            d = {}
            for i in nums:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            return len([ele for ele in d.values() if ele >= 2])
        
        elif k<0:
            return 0
        
        d = {}
        s = set()
        
        for i in nums:
            if i not in d:
                d[i] = 1
            
        for j in d.keys():
            plus, minus = j+k, j-k
            if plus in d:
                s.add((j,plus))
            if minus in d:
                s.add((minus, j))
        
        return len(s)