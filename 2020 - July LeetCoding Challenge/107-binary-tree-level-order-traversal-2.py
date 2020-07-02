# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
    Given binary tree [3,9,20,null,null,15,7],
          3
         / \
        9  20
          /  \
         15   7
    return its bottom-up level order traversal as:
        [
        [15,7],
        [9,20],
        [3]
        ]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        answer = []
        queue = [root]
        
        while queue:
            next_level_nodes = []
            curr_level_nodes = []
            
            for node in queue:
                curr_level_nodes.append(node.val)
                
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
                    
            queue = next_level_nodes
            answer.insert(0, curr_level_nodes)
        
        return answer