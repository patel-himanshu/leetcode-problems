# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3435/

"""
Find the sum of all left leaves in a given binary tree.

Example:
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        
        def inorder(root):
            if not root: return
            if root.left:
                if not root.left.left and not root.left.right:
                    self.ans += root.left.val
                inorder(root.left)
            
            if root.right:
                inorder(root.right)
            
        inorder(root)
        return self.ans