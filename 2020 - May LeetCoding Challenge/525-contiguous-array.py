# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3341/

"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000. 
"""

class Solution:
    def findMaxLength(self, nums):      # findMaxLength(self, nums: List[int]) -> int
        # Replacing all 0 with -1
        new_nums = [-1 if i==0 else 1 for i in nums] 
        
        size = len(nums)
        total = 0
        cum_sum = [0]*size
        indices = {}    # Hash table with first and last occurrence of an element
        max_len = 0
        
        # Creating cummulative sum list and hash table
        for i in range(size):
            total += new_nums[i]
            cum_sum[i] = total

            if cum_sum[i] == 0:
                max_len = i+1

            if cum_sum[i] in indices.keys():
                indices[cum_sum[i]][1] = i
            else:
                indices[cum_sum[i]] = [i,i]

        # Calculating element with maximum distance between its first and last occurrence
        for i in indices:
            max_len = max(max_len, indices[i][1]-indices[i][0])
        return max_len        

inputs = [
    [0,1],
    [0,1,0],
    [0,0,0,0],
    [0,1,0,1],
    [0,1,0,1,0],
    [0,0,0,1,1,1],
    [0,0,1,0,1,1,0],
    [0,0,1,0,0,0,1,1],
    [0,0,1,1,1,1,1,0,1,0],
]

outputs = [2,2,0,4,4,6,6,6,4]

S = Solution()
for i in range(len(outputs)):
    print(S.findMaxLength(inputs[i]))