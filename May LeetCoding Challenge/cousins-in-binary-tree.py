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