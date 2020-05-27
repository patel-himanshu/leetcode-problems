# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3342/

"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:
    Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: group1 [1,4], group2 [2,3]

Example 2:
    Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false

Example 3:
    Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    Output: false

Note:
    (1) 1 <= N <= 2000
    (2) 0 <= dislikes.length <= 10000
    (3) 1 <= dislikes[i][j] <= N
    (4) dislikes[i][0] < dislikes[i][1]
    (5) There does not exist i != j for which dislikes[i] == dislikes[j].
"""

from collections import defaultdict

class Solution:
    def possibleBipartition(self, N, dislikes): # possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool
        neighbours = defaultdict(list)

        # Creating a list of disliked neighbours, for each person in the group
        for a,b in dislikes:
            neighbours[a-1].append(b-1)
            neighbours[b-1].append(a-1)

        # If an element (node) has not been visited, then colors[element] = 0
        # Later its value becomes 1 or -1, depending upon the group it belongs to
        colors = [0]*N

        def no_neighbour_color_conflict(person, color):
            # Change the color of node, as it no longer remains unvisited
            colors[person] = color

            for neighbour in neighbours[person]:
                # If a node has already been visited, then compare its color 
                # with the color of its parent node
                if colors[neighbour] == color:
                    return False
                
                # If a node has not been visited, then visit it, and check for color conflict
                # If given node doesn't have the color of any group, 
                # then assign it the color of opposite group of that of its parent
                if colors[neighbour] == 0 and not no_neighbour_color_conflict(neighbour, -color):
                    return False
            return True

        for i in range(N):
            # Check whether given element has been visited or not
            # If not visited, then visit it and then check for color conflict for each of its neighbours
            # If there is any conflict in color of any of its neighbour, return "True"
            if colors[i] == 0 and not no_neighbour_color_conflict(i,1):
                return False

        # No conflicts were found, hence it can be resolved into 2 groups
        return True

inputs1 = [1,2,4,3,5]

inputs2 = [
    [],
    [],
    [[1,2],[1,3],[2,4]],
    [[1,2],[1,3],[2,3]],
    [[1,2],[2,3],[3,4],[4,5],[1,5]]
]

outputs = [True, True, True, False, False]

S = Solution()
for i in range(len(inputs1)):
    print(S.possibleBipartition(inputs1[i], inputs2[i]))