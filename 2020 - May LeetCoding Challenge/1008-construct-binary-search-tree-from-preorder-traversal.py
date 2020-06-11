# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3339/

"""
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of 
node.left has a value < node.val, and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:
    Input: [8,5,1,7,10,12]
    Output: [8,5,10,1,7,null,12]
                8
               / \ 
              5   10
             / \    \ 
            1   7    12

Constraints:
    (1) 1 <= preorder.length <= 100
    (2) 1 <= preorder[i] <= 10^8
    (3) The values of preorder are distinct.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):    # bstFromPreorder(self, preorder: List[int]) -> TreeNode
        bst_size = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, bst_size):
            temp = None

            while stack and preorder[i] > stack[-1].val:
                temp = stack.pop()
            
            if temp:
                temp.right = TreeNode(preorder[i])
                stack.append(temp.right)
            else:
                temp = stack[-1]
                temp.left = TreeNode(preorder[i])
                stack.append(temp.left)
            
            # stack.append(TreeNode(preorder[i]))
            """ 
            Above statement just appends a node in stack.
            This causes the loss of linkage between the nodes.
            We just have individual nodes in the stack.
            """

        return root