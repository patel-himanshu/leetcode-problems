# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3443/

"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
    (1) Search for a node to remove.
    (2) If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:
    root = [5,3,6,2,4,null,7]
    key = 3
            5
           / \
          3   6
         / \   \
        2   4   7
    Given key to delete is 3. So we find the node with value 3 and delete it.

    One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
            5
           / \
          4   6
         /     \
        2       7

    Another valid answer is [5,2,6,null,4,null,7].
            5
           / \
          2   6
           \   \
            4   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        elems = []
        
        def inorder(node):
            if not node: return
            elems.append(node.val)
            if node.left: inorder(node.left)
            if node.right: inorder(node.right)
        
        inorder(root)
        if key in elems:
            elems.remove(key)
        elems.sort()

        start, stop = 0, len(elems)-1

        def list2bst(start, stop):
            if start > stop:
                return
            
            mid = (start + stop) // 2
            new_root = TreeNode(elems[mid])
            new_root.left = list2bst(start, mid-1)
            new_root.right = list2bst(mid+1, stop)
            return new_root
    
        return list2bst(start, stop)