# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3393/

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Note:
    (1) You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    (2) Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    (3) It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    (4) You can return the answer in any order.
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count.items(), key = lambda x: x[1], reverse = True)
        ans = []
        i = 0
        while i != k:
            ans.append(sorted_count[i][0])
            i += 1
        return ans