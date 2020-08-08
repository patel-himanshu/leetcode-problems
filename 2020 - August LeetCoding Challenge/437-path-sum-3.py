# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3417/

"""
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
              10
             /  \
            5   -3
           / \    \
          3   2   11
         / \   \
        3  -2   1
    Return 3. The paths that sum to 8 are:
        1.  5 -> 3
        2.  5 -> 2 -> 1
        3. -3 -> 11
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = 0
    
    def pathSum(self, root: TreeNode, sum: int) -> int:    
        def dfs(node, prev_sum, start=False):
            if not node:
                return None
            
            new_sum = prev_sum + node.val
            
            if new_sum == sum:
                self.ans += 1
        
            dfs(node.left, new_sum)
            dfs(node.right, new_sum)
            
            if start:
                dfs(node.left, 0, True)
                dfs(node.right, 0, True)
        
        dfs(root, 0, True)
        return self.ans