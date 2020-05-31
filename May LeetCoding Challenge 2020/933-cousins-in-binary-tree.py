# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false
            1
           / \ 
          2   3
         /
        4

Example 2:
    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true
            1
           / \ 
          2   3
           \   \ 
            4   5

Example 3:
    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false
            1
           / \ 
          2   3
           \ 
            4

Constraints:
    (1) The number of nodes in the tree will be between 2 and 100.
    (2) Each node has a unique integer value from 1 to 100.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Function to find level of a node 
    def getLevel(self, root, data, level):
        if root == None:
            return 0
        elif root.val == data:
            return level
        
        currLevel = self.getLevel(root.left, data, level+1)
        if currLevel != 0:
            return currLevel
        
        currLevel = self.getLevel(root.right, data, level+1)
        return currLevel
        
    # Function to find the parent of a node
    def findParent(self, root, parentData, data):
        if root == None:
            return 0
        elif root.val == data:
            return parentData
        
        currParent = self.findParent(root.left, root.val, data)
        if currParent != 0:
            return currParent
        
        currParent = self.findParent(root.right, root.val, data)
        return currParent
        
    # Function to find whether given nodes are cousins or not
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        a = self.getLevel(root, x, 1)
        b = self.getLevel(root, y, 1)
        
        if a == b:
            if self.findParent(root, -1, x) != self.findParent(root, -1, y):
                return True
        return False