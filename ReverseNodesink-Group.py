# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Hàm để đảo ngược thứ tự của một đoạn gồm k nút
        def reverse_group(start, end):
            prev = None
            current = start
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        # Kiểm tra xem có đủ k nút để đảo ngược không
        count = 0
        current = head
        while current and count < k:
            current = current.next
            count += 1
        if count < k:
            return head
        
        # Đảo ngược thứ tự của k nút đầu tiên
        new_head = reverse_group(head, current)
        
        # Đệ quy để đảo ngược các đoạn k tiếp theo
        head.next = self.reverseKGroup(current, k)
        
        return new_head
