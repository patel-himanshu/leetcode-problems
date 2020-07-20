# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3396/

"""
Remove all elements from a linked list of integers that have value val.

Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        
        temp = head
        
        while head and head.val == val:
            if temp.next:
                temp = temp.next
                head.next = None
                head = temp
            else:
                return None
        
        if not head: return head
        
        temp = temp.next
        prev = head
        
        while temp:
            if temp.val == val:
                prev.next = temp.next
                temp = prev.next
            else:
                prev = prev.next
                temp = temp.next
                
        return head