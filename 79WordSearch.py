class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(row, col, index):
            # Kiểm tra xem đã tìm thấy từ cần tìm kiếm chưa
            if index == len(word):
                return True
            
            # Kiểm tra điều kiện giới hạn của ô
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
                return False
            
            # Lưu giá trị của ô hiện tại và đánh dấu ô này đã được sử dụng
            temp = board[row][col]
            board[row][col] = ''
            
            # Duyệt qua các ô kế tiếp
            if backtrack(row + 1, col, index + 1) or \
               backtrack(row - 1, col, index + 1) or \
               backtrack(row, col + 1, index + 1) or \
               backtrack(row, col - 1, index + 1):
                return True
            
            # Khôi phục giá trị của ô và quay lại trạng thái trước đó
            board[row][col] = temp
            return False
        
        # Duyệt qua tất cả các ô trong bảng
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
