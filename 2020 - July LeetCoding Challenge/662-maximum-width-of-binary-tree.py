# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3385/

"""
Given a binary tree, write a function to get the maximum width of the given tree.
The width of a tree is the maximum width among all levels.
The binary tree has the same structure as a full binary tree, but some nodes are null.
The width of one level is defined as the length between the end-nodes (the leftmost and right most 
non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
    Input: 
             1
           /   \
          3     2
         / \     \  
        5   3     9 
    Output: 4
    Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:
    Input: 
            1
           /  
          3    
         / \       
        5   3     
    Output: 2
    Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:
    Input: 
            1
           / \
          3   2 
         /        
        5      
    Output: 2
    Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:
    Input: 
              1
             / \
            3   2
           /     \  
          5       9 
         /         \
        6           7
    Output: 8
    Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

Note: Answer will in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        
        queue = [(root, 1)]
        width = 1
        last_node = root
        
        while queue:
            node, index = queue.pop(0)
            
            if node.left:
                queue.append((node.left, index*2))
            if node.right:
                queue.append((node.right, index*2 + 1))
                
            if node == last_node:
                if len(queue):
                    last_node = queue[-1][0]
                    width = max(width, queue[-1][1] - queue[0][1] + 1)
        
        return width