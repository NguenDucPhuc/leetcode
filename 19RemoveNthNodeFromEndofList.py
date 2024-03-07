# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Tạo nút giả trước đầu danh sách
        dummy = ListNode(0)
        dummy.next = head
        
        # Sử dụng hai con trỏ
        first = dummy
        second = dummy
        
        # Di chuyển con trỏ thứ hai n bước
        for _ in range(n + 1):
            second = second.next
        
        # Di chuyển cả hai con trỏ cùng một lượng bước cho đến khi con trỏ thứ hai đến cuối danh sách
        while second is not None:
            first = first.next
            second = second.next
        
        # Loại bỏ nút thứ n từ cuối danh sách
        first.next = first.next.next
        
        return dummy.next
