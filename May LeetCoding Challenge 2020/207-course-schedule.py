# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3344/

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.

Constraints:
    (1) The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    (2) You may assume that there are no duplicate edges in the input prerequisites.
    (3) 1 <= numCourses <= 10^5
"""
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def is_cyclic_checker(self, node, visited, recursion_stack):
        visited[node] = True
        recursion_stack[node] = True

        for connected_node in self.graph[node]:
            if recursion_stack[connected_node]:
                return True
            elif not visited[connected_node]:
                if self.is_cyclic_checker(connected_node, visited, recursion_stack):
                    return True
                    
        recursion_stack[node] = False
        return False

    def canFinish(self, numCourses, prerequisites): # canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool
        
        # Creating adjacency list representation of the graph
        for start_node, end_node in prerequisites:
            self.graph[start_node].append(end_node)

        visited = [False]*numCourses
        recursion_stack = [False]*numCourses

        # Checking presence of cycle using DFS
        for node in range(numCourses):
            if not visited[node]:
                if self.is_cyclic_checker(node, visited, recursion_stack):
                    return False
        return True
        
    
inputs = [
    [5, [[1,0]]],
    [2, [[1,0]]],
    [2, [[1,0], [0,1]]],
    [3, [[2,1], [1,0]]],
    [4, [[3,0], [0,1]]],
    [5, [[3,1], [2,0]]],
    [3, [[2,1], [1,0], [0,2]]],
    [4, [[3,2], [2,1], [1,2], [1,0]]],
    [4, [[3,2], [2,1], [1,2], [1,0], [1,3]]]
]
outputs = [True, True, False, True, True, True, False, False, False]

for i in range(len(inputs)):
    S = Solution()
    print('Case {}: {}'.format(i+1,S.canFinish(inputs[i][0], inputs[i][1]) == outputs[i]))