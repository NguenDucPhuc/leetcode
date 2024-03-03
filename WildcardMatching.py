class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Khởi tạo bảng lưu trữ các kết quả đã tính
        memo = {}
        
        def dp(i, j):
            # Kiểm tra xem đã tính toán kết quả cho cặp (i, j) chưa
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Nếu đã duyệt hết cả hai chuỗi, kiểm tra xem có khớp không
            if i == len(s) and j == len(p):
                return True
            # Nếu chỉ có chuỗi pattern còn lại, kiểm tra xem tất cả đều là '*'
            elif j == len(p):
                return False
            # Nếu chỉ có chuỗi input còn lại
            elif i == len(s):
                # Kiểm tra xem tất cả các ký tự còn lại trong pattern có phải là '*'
                return all(p[k] == '*' for k in range(j, len(p)))
            
            # Nếu ký tự tương ứng là '?' hoặc giống nhau, tiếp tục đệ quy với các ký tự tiếp theo
            if p[j] == '?' or p[j] == s[i]:
                ans = dp(i + 1, j + 1)
            # Nếu ký tự là '*', có thể phù hợp với 0 ký tự hoặc một chuỗi ký tự
            elif p[j] == '*':
                ans = dp(i + 1, j) or dp(i, j + 1)
            # Nếu không khớp, gán False cho kết quả
            else:
                ans = False
            
            # Lưu kết quả vào bảng lưu trữ và trả về
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)
