# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Khởi tạo một node giả đầu dùng để trỏ tới kết quả
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Duyệt qua cả hai danh sách liên kết đầu vào cùng một lúc
        while l1 or l2:
            # Lấy giá trị của các node hiện tại hoặc 0 nếu không có node
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Tính tổng và cập nhật giá trị cộng dồn (carry)
            total = val1 + val2 + carry
            carry = total // 10

            # Tạo một node mới chứa phần dư của tổng
            current.next = ListNode(total % 10)
            current = current.next

            # Di chuyển đến node tiếp theo trong cả hai danh sách nếu có
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Nếu còn phần cộng dồn (carry), thêm một node cuối cùng vào kết quả
        if carry > 0:
            current.next = ListNode(carry)

        # Trả về node đầu tiên của kết quả, loại bỏ node giả đầu
        return dummy_head.next
