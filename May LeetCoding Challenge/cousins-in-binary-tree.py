# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkLevel(self, root, data, level):
        if root == None:
            return 0
        elif root.val == data:
            return level
        
        currLevel = self.checkLevel(root.left, data, level+1)
        if currLevel != 0:
            return currLevel
        
        currLevel = self.checkLevel(root.right, data, level+1)
        return currLevel
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xLevel = self.checkLevel(root, x, 1)
        yLevel = self.checkLevel(root, y, 1)
        if xLevel == yLevel:
            return True
        else:
            return False



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        visited = []
        if root:
            visited.append(root)
        current = visited[0]
        while current:
            if current.left:
                visited.append(current.left)
                if current.left == x:
                    a = 1
                elif current.left == y:
                    b = 1
            elif current.right:
                visited.append(current.right)
                if current.right == x:
                    a = 1
                elif current.right == y:
                    b = 1
            visited.pop(0)
            if not visited:
                break
            current = visited[0]