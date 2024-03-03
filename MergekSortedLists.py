# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Hàm gộp hai danh sách liên kết đã sắp xếp
        def mergeTwoLists(l1, l2):
            # Tạo một nút giả để làm nút đầu của danh sách kết quả
            dummy = ListNode(0)
            # Khởi tạo một con trỏ hiện tại để duyệt qua danh sách kết quả
            current = dummy
            # Duyệt qua cả hai danh sách và gộp chúng lại
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            # Nối danh sách còn lại vào danh sách kết quả
            current.next = l1 if l1 else l2
            # Trả về danh sách kết quả bắt đầu từ nút giả
            return dummy.next
        
        # Nếu danh sách trống hoặc chỉ chứa một danh sách liên kết
        if not lists or len(lists) == 1 and not lists[0]:
            return None if not lists or len(lists) == 1 and not lists[0] else lists[0]
        
        # Sử dụng phương pháp chia để trị để gộp danh sách liên kết
        while len(lists) > 1:
            # Khởi tạo một danh sách mới để chứa danh sách đã gộp
            new_lists = []
            # Duyệt qua danh sách các danh sách liên kết ban đầu theo từng cặp
            for i in range(0, len(lists), 2):
                # Lấy hai danh sách liên kết từ danh sách ban đầu
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                # Gộp hai danh sách liên kết và thêm vào danh sách mới
                new_lists.append(mergeTwoLists(l1, l2))
            # Cập nhật danh sách ban đầu với danh sách mới
            lists = new_lists
        
        # Trả về danh sách kết quả
        return lists[0]
