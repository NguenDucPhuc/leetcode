class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Loại bỏ các khoảng trắng ở đuôi chuỗi
        s = s.rstrip()
        # Tìm độ dài của từ cuối cùng trong chuỗi s sau khi đã loại bỏ các khoảng trắng ở đuôi
        length = 0
        for char in reversed(s):
            if char == ' ':
                break
            length += 1
        return length
