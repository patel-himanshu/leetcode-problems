# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3314/

"""
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node
 to any node in the tree along the parent-child connections. 
 The path must contain at least one node and does not need to go through the root.

Example 1:
    Input: [1,2,3]
            1
           / \
          2   3
    Output: 6

Example 2:
    Input: [-10,9,20,null,null,15,7]
           -10
           / \
          9  20
            /  \
           15   7
    Output: 42
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            max_lr = max(left, right)
            max_single_node = max(node.val, node.val + max_lr)
            max_total = max(node.val + left + right, max_single_node)
            self.result = max(self.result, max_total)
            return max_single_node
        
        helper(root)
        return self.result