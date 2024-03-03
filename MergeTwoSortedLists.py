# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Khởi tạo một node giả để dễ quản lý
        dummy = ListNode(-1)
        # Node hiện tại của merged list
        current = dummy
        
        # Duyệt qua cả hai danh sách
        while l1 and l2:
            # So sánh giá trị của hai node, thêm node có giá trị nhỏ hơn vào merged list
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            # Di chuyển current pointer đến phần tử tiếp theo của merged list
            current = current.next
        
        # Kiểm tra nếu một trong hai danh sách đã hết, thêm phần còn lại vào merged list
        if l1:
            current.next = l1
        else:
            current.next = l2
        
        # Trả về head của merged list (bỏ qua node giả)
        return dummy.next
