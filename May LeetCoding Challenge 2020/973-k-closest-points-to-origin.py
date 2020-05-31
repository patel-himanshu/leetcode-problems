# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/

"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
    Input: points = [[1,3],[-2,2]], K = 1
    Output: [[-2,2]]
    Explanation: The distance between (1, 3) and the origin is sqrt(10).
                 The distance between (-2, 2) and the origin is sqrt(8).
                 Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
                 We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], K = 2
    Output: [[3,3],[-2,4]]
            (The answer [[-2,4],[3,3]] would also be accepted.)

Note:
    (1) 1 <= K <= points.length <= 10000
    (2) -10000 < points[i][0] < 10000
    (3) -10000 < points[i][1] < 10000
"""
from math import sqrt
from operator import itemgetter

class Solution:
    def kClosest(self, points, K):   # kClosest(self, points: List[List[int]], K: int) -> List[List[int]]
        distances = []

        for i in points:
            distance = sqrt((i[0])**2 + (i[1])**2)
            distances.append(distance)
        
        combined = sorted(zip(points, distances), key=itemgetter(1))
        ans = []

        for k in range(K):
            ans.append(combined[k][0])
        
        return ans

inputs = [
    [[[1,3], [-2,2]], 1],
    [[[3,3],[5,-1],[-2,4]], 2]
]

outputs = [
    [[-2,2]],
    [[3,3],[-2,4]]
]

S = Solution()
for i in range(len(inputs)):
    print('Case {}: {}'.format(i+1, S.kClosest(inputs[i][0], inputs[i][1]) == outputs[i]))