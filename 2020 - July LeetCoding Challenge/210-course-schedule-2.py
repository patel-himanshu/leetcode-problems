# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3394/

"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:
    Input: 2, [[1,0]] 
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
                course 0. So the correct course order is [0,1] .

Example 2:
    Input: 4, [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
                courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
                So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:
    (1) The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    (2) You may assume that there are no duplicate edges in the input prerequisites.
"""

from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:      
        
        self.graph = defaultdict(list)
        self.visited = [0] * numCourses
        self.answer = []
        
        for start_node, end_node in prerequisites:
            self.graph[start_node].append(end_node)
            
        for i in range(numCourses):
            if self.visited[i] != 1:
                is_valid = self.dfs(i)
                if not is_valid:
                    return []
        
        return self.answer

    def dfs(self, node_index):
            
        if self.visited[node_index] == -1: # Indicates presence of cycle in the graph
            return False
        
        if self.visited[node_index] == 1: # Indicates that present node has already been visited
            return True
        
        self.visited[node_index] = -1 # Present node is been fixed as source node
        flag = True
        
        for node in self.graph[node_index]:
            flag = flag and self.dfs(node)
            
        self.visited[node_index] = 1 # DFS has been applied on the present node, and no cycle was detected
        self.answer.append(node_index)
        
        return flag