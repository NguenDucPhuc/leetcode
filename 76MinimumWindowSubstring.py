class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        
        # Hàm kiểm tra xem cửa sổ hiện tại có chứa tất cả các ký tự trong chuỗi t không
        def isValid(window_counts, target_counts):
            for char, count in target_counts.items():
                if window_counts[char] < count:
                    return False
            return True
        
        if not s or not t:
            return ""
        
        # Đếm tần suất xuất hiện của các ký tự trong chuỗi t
        target_counts = Counter(t)
        
        # Khởi tạo các biến
        required = len(target_counts)
        left, right = 0, 0
        formed = 0
        window_counts = {}
        
        # Biến lưu trữ kết quả
        ans = float("inf"), None, None
        
        while right < len(s):
            # Thêm ký tự mới vào cửa sổ
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Kiểm tra xem cửa sổ hiện tại có chứa tất cả các ký tự trong chuỗi t không
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            
            # Thu hẹp cửa sổ
            while left <= right and formed == required:
                char = s[left]
                
                # Cập nhật kết quả nếu cần
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Loại bỏ ký tự từ cửa sổ
                window_counts[char] -= 1
                if char in target_counts and window_counts[char] < target_counts[char]:
                    formed -= 1
                
                # Di chuyển cửa sổ sang phải
                left += 1
            
            # Di chuyển cửa sổ sang phải
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
