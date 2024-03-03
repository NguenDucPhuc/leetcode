class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, combination):
            # Nếu đã chọn đủ k số, thêm danh sách này vào danh sách kết quả cuối cùng
            if len(combination) == k:
                result.append(combination[:])
                return
            
            # Duyệt qua các số từ start đến n
            for i in range(start, n + 1):
                # Thêm số hiện tại vào danh sách kết quả tạm thời
                combination.append(i)
                # Duyệt tiếp tục với start là số tiếp theo
                backtrack(i + 1, combination)
                # Sau khi duyệt xong một nhánh, loại bỏ số hiện tại để thử các số khác
                combination.pop()
        
        result = []
        backtrack(1, [])
        return result
