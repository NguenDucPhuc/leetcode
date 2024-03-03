class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Khởi tạo một stack
        stack = []
        
        # Tạo một từ điển lưu trữ các cặp ngoặc
        brackets = {')': '(', '}': '{', ']': '['}
        
        # Duyệt qua từng ký tự trong chuỗi
        for char in s:
            # Nếu là ký tự mở ngoặc, đưa vào stack
            if char in brackets.values():
                stack.append(char)
            # Nếu là ký tự đóng ngoặc
            elif char in brackets.keys():
                # Nếu stack rỗng hoặc ký tự mở ngoặc không tương ứng
                if not stack or stack.pop() != brackets[char]:
                    return False
        
        # Nếu stack còn phần tử, tức là còn ký tự mở ngoặc chưa được đóng
        return not stack
