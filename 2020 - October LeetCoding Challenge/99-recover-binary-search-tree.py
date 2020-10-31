# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3514/

"""
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Example 1:
    Input: root = [1,3,null,null,2]
    Output: [3,1,null,null,2]
    Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
    Input: root = [3,1,4,null,null,2]
    Output: [2,1,4,null,null,3]
    Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:
    (1) The number of nodes in the tree is in the range [2, 1000].
    (2) -2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        cur, node, cands = root, TreeNode(-float("inf")), []
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if cur.val < node.val:
                        cands += [node, cur]
                    node = cur
                    cur = cur.right
            else:
                if cur.val < node.val:
                    cands += [node, cur]
                node = cur
                cur = cur.right
            
        cands[0].val, cands[-1].val = cands[-1].val, cands[0].val