# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3493/

"""
Given the head of a linked list, return the list after sorting it in ascending order.
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Example 3:
    Input: head = []
    Output: []

Constraints:
    (1) The number of nodes in the list is in the range [0, 5 * 104].
    (2) -105 <= Node.val <= 105
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1, list2):
        dummy = ListNode(0)
        temp = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
            
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return dummy.next
    
    def get_mid(self, head):
        temp = head
        mid_prev = None
        
        while temp and temp.next:
            if mid_prev is None:
                mid_prev = head
            else:
                mid_prev = mid_prev.next
            temp = temp.next.next
        
        mid = mid_prev.next
        mid_prev.next = None
        return mid
        
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)