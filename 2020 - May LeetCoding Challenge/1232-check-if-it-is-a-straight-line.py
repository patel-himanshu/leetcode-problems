# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/

"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true

Example 2:
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false

Constraints:
    (1) 2 <= coordinates.length <= 1000
    (2) coordinates[i].length == 2
    (3) -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    (4) coordinates contains no duplicate point.
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m1_num = coordinates[1][1] - coordinates[0][1]
        m1_den = coordinates[1][0] - coordinates[0][0]
        if m1_den == 0:
            m1 = None
        else:
            m1 = m1_num/m1_den
        for i in range(1, len(coordinates)-1):
            m2_num = coordinates[i+1][1] - coordinates[i][1]
            m2_den = coordinates[i+1][0] - coordinates[i][0]
            if m2_den == 0:
                m2 = None
            else:
                m2 = m2_num/m2_den
            if m1!= m2:
                return False
        return True