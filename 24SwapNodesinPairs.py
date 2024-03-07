# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Kiểm tra nếu danh sách rỗng hoặc chỉ có một nút
        if not head or not head.next:
            return head
        
        # Lưu nút tiếp theo của cặp nút hiện tại
        next_node = head.next
        
        # Đổi chỗ giá trị của hai nút trong cặp hiện tại
        head.next = self.swapPairs(next_node.next)
        next_node.next = head
        
        # Trả về nút tiếp theo của cặp đã đảo chỗ
        return next_node
