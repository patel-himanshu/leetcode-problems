# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3438/

"""
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than 
or equal to the end point of the interval i, which can be called that j is on the "right" of i.
For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point 
to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i.
Finally, you need output the stored value of each interval as an array.

Note:
    (1) You may assume the interval's end point is always bigger than its start point.
    (2) You may assume none of these intervals have the same start point.

Example 1:
    Input: [ [1,2] ]
    Output: [-1]
    Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
    Input: [ [3,4], [2,3], [1,2] ]
    Output: [-1, 0, 1]
    Explanation: There is no satisfied "right" interval for [3,4].
                For [2,3], the interval [3,4] has minimum-"right" start point;
                For [1,2], the interval [2,3] has minimum-"right" start point.

Example 3:
    Input: [ [1,4], [2,3], [3,4] ]
    Output: [-1, 2, -1]
    Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
                For [2,3], the interval [3,4] has minimum-"right" start point.
"""

class Solution:
    def binarySearch(self, arr, val):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (high + low) // 2
            if arr[mid][1][0] == val:
                return mid
            elif arr[mid][1][0] < val:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:        
        n = len(intervals)
        res = [-1] * n
        check_list = list(sorted([(i, val) for i, val in enumerate(intervals)], key=lambda x: x[1][0]))

        for i, interval in enumerate(intervals):
            val = interval[1]
            idx = self.binarySearch(check_list, val)
            if idx < n:
                res[i] = check_list[idx][0]
        return res