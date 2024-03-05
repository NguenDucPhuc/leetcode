class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Bỏ qua các khoảng trắng đầu tiên
        s = s.strip()

        # Kiểm tra xem chuỗi có rỗng không
        if not s:
            return 0

        # Xác định dấu của số
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Xây dựng số nguyên từ các ký tự trong chuỗi
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Áp dụng dấu và giới hạn của số nguyên 32-bit
        result *= sign
        result = max(-2**31, min(result, 2**31 - 1))

        return result
