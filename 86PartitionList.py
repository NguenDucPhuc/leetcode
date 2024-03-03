# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller_head = ListNode(0)
        smaller_tail = smaller_head
        greater_head = ListNode(0)
        greater_tail = greater_head
        
        current = head
        
        while current:
            if current.val < x:
                smaller_tail.next = current
                smaller_tail = smaller_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            
            current = current.next
        
        greater_tail.next = None
        smaller_tail.next = greater_head.next
        
        return smaller_head.next
