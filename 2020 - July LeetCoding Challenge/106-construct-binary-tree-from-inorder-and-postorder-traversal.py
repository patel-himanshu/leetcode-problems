# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3403/

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.

Example:
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    Return the following binary tree:
        3
       / \
      9  20
        /  \
       15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
        if len(inorder) == 1: return TreeNode(inorder[0])
        
        root = TreeNode(postorder[-1])
        pos = inorder.index(root.val)
        root.left = self.buildTree(inorder[: pos], postorder[: pos])
        root.right = self.buildTree(inorder[pos+1 :], postorder[pos : -1])
        return root