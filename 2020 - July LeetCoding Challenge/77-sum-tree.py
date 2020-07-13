# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3389/

"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
    Input:     1         1
              / \       / \
             2   3     2   3
    
            [1,2,3],   [1,2,3]
    Output: true

Example 2:
    Input:     1         1
              /           \
             2             2
    
            [1,2],     [1,null,2]
    Output: false

Example 3:
    Input:     1         1
              / \       / \
             2   1     1   2
    
            [1,2,1],   [1,1,2]
    Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return True if not p and not q else False