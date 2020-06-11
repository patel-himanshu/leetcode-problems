# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/

"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b. 
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
    Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

Note:
    (1) 0 <= A.length < 1000
    (2) 0 <= B.length < 1000
    (3) 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""

class Solution:
    def intervalIntersection(self, A, B): # intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]
        ans = []
        a, b = 0, 0

        while a<len(A) and b<len(B):
            a_lower = A[a][0]
            a_upper = A[a][1]
            b_lower = B[b][0]
            b_upper = B[b][1]

            if a_upper == b_lower:                              # A = [4,6], B = [6,8]
                ans.append([a_upper, b_lower])                  # Intersection = [6,6]
                a += 1

            elif b_upper == a_lower:                            # A = [4,6], B = [2,4]
                ans.append([b_upper, a_lower])                  # Intersection = [4,4]
                b += 1

            elif a_lower <= b_lower < a_upper <= b_upper:       # A = [0,3], B = [2,4]
                ans.append([b_lower, a_upper])                  # Intersection = [2,3]
                a += 1

            elif b_lower <= a_lower < b_upper <= a_upper:       # A = [2,4], B = [0,3]
                ans.append([a_lower, b_upper])                  # Intersection = [2,3]
                b += 1

            elif b_lower <= a_lower <= a_upper <= b_upper:      # A = [4,5], B = [2,8]
                ans.append([a_lower, a_upper])                  # Intersection = [4,5]
                a += 1

            elif a_lower <= b_lower <= b_upper <= a_upper:      # A = [2,8], B = [4,5]
                ans.append([b_lower, b_upper])                  # Intersection = [4,5]
                b += 1

            elif b_lower > a_upper:                             # A = [0,2], B = [3,5]
                a += 1                                          # Intersection = []

            elif a_lower > b_upper:                             # A = [3,5], B = [0,2]
                b += 1                                          # Intersection = []

        return ans

inputs_A = [   
    [[0,2],[5,10],[13,23],[24,25]],
    [[3,5],[9,20]]
]

inputs_B = [   
    [[1,5],[8,12],[15,24],[25,26]], 
    [[4,5],[7,10],[11,12],[14,15],[16,20]]
]

outputs = [
    [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]],
    [[4,5],[9,10],[11,12],[14,15],[16,20]]
]

S = Solution()
for i in range(len(outputs)):
    result = S.intervalIntersection(inputs_A[i], inputs_B[i])
    if result == outputs[i]:
        print("Case {}: Pass".format(i+1))
    else:
        print("Case {}: Fail".format(i+1))