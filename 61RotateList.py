# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Nếu danh sách rỗng hoặc chỉ có một nút, hoặc k = 0, không cần xoay, trả về ngay
        if not head or not head.next or k == 0:
            return head
        
        # Đếm số lượng nút trong danh sách
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Tính số bước xoay thực sự cần thực hiện
        k %= length
        
        # Nếu k = 0, không cần xoay, trả về ngay
        if k == 0:
            return head
        
        # Di chuyển con trỏ cuối danh sách đến nút cuối cùng
        current.next = head
        
        # Di chuyển con trỏ tới vị trí mới của đầu danh sách
        for _ in range(length - k):
            current = current.next
        
        # Lấy nút tiếp theo của con trỏ mới làm đầu danh sách mới
        new_head = current.next
        # Cắt liên kết tại vị trí của con trỏ mới
        current.next = None
        
        return new_head
