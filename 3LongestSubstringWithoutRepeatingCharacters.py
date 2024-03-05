class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Khởi tạo một từ điển để lưu trữ vị trí xuất hiện của các ký tự trong chuỗi
        char_index = {}
        max_length = 0
        start = 0

        # Duyệt qua từng ký tự trong chuỗi
        for end, char in enumerate(s):
            # Kiểm tra xem ký tự đã xuất hiện trước đó hay không
            if char in char_index and char_index[char] >= start:
                # Nếu ký tự đã xuất hiện và nằm trong phạm vi của chuỗi con hiện tại
                # Cập nhật lại vị trí bắt đầu của chuỗi con
                start = char_index[char] + 1

            # Cập nhật lại vị trí xuất hiện của ký tự
            char_index[char] = end

            # Cập nhật độ dài của chuỗi con không lặp lại dài nhất
            max_length = max(max_length, end - start + 1)

        return max_length
