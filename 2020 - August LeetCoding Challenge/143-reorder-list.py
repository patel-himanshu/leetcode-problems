# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3430/

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
    Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        nodes = []
        temp = head
        
        while temp:
            nodes.append(temp)
            temp = temp.next

        for i in range(len(nodes)//2):
            nodes[i].next, nodes[-(i+1)].next = nodes[-(i+1)], nodes[i+1]
        
        nodes[len(nodes)//2].next = None
        return