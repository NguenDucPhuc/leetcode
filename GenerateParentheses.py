class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(s="", left=0, right=0):
            # Nếu độ dài của chuỗi s đạt đến 2*n, thêm chuỗi s vào kết quả
            if len(s) == 2 * n:
                result.append(s)
                return
            # Nếu số lượng dấu ngoặc mở chưa đạt n, thêm dấu ngoặc mở vào chuỗi s và tiếp tục đệ quy
            if left < n:
                backtrack(s + "(", left + 1, right)
            # Nếu số lượng dấu ngoặc đóng chưa đạt số lượng dấu ngoặc mở, thêm dấu ngoặc đóng vào chuỗi s và tiếp tục đệ quy
            if right < left:
                backtrack(s + ")", left, right + 1)

        # Khởi tạo biến chứa kết quả
        result = []
        # Gọi hàm backtrack để tạo chuỗi ngoặc đúng
        backtrack()
        # Trả về kết quả
        return result

# Example usage:
n = 3
solution = Solution()
print(solution.generateParenthesis(n))
