class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Khởi tạo stack với chỉ số -1
        max_length = 0  # Khởi tạo độ dài lớn nhất của chuỗi ngoặc hợp lệ
        
        # Duyệt qua chuỗi
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Đẩy chỉ số của '(' vào stack
            else:
                stack.pop()  # Loại bỏ '(' khỏi stack cho mỗi ')'
                if not stack:
                    stack.append(i)  # Nếu stack trở thành rỗng, đẩy chỉ số của ')' hiện tại vào stack
                else:
                    max_length = max(max_length, i - stack[-1])  # Cập nhật độ dài lớn nhất
                    
        return max_length



