# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3335/

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
                  3
                 / \
                1   4
                 \
                  2
    Output: 1

Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
                     5
                    / \
                   3   6
                  / \
                 2   4
                /
               1
    Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.elements = []

    def InOrder(self, root):
        if root:
            self.InOrder(root.left)
            if root.val >= 0:
                self.elements.append(root.val)
            self.InOrder(root.right)

    def kthSmallest(self, root, k): # kthSmallest(self, root: TreeNode, k: int) -> int
        self.InOrder(root)
        return self.elements[k-1]

input1 = [
    [3,1,4,null,2],
    [5,3,6,2,4,null,null,1],
    [41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]
]

input2 = [1, 3, 25]

answer = [1, 3, 25]