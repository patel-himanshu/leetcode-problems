# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3398/

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
        [
        [3],
        [20,9],
        [15,7]
        ]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        
        answer = []
        queue = [root]
        level = 0
        
        while queue:
            curr_level_nodes = []
            next_level_nodes = []
            
            for node in queue:
                curr_level_nodes.append(node.val)
                
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
                    
            queue = next_level_nodes
            level += 1
            
            if level & 1:
                answer.append(curr_level_nodes)
            else:
                answer.append(curr_level_nodes[::-1])
        
        return answer