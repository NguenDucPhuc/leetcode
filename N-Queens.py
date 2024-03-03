class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # Khởi tạo một danh sách để lưu trữ kết quả
        self.result = []
        # Khởi tạo một danh sách để lưu trữ cấu hình của bàn cờ
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        # Gọi hàm đệ quy để tìm tất cả các cách sắp xếp n-queens
        self.solve(0, n)
        return self.result
    
    def solve(self, row, n):
        # Nếu đã xử lý hết các hàng, thêm cấu hình bàn cờ vào kết quả
        if row == n:
            self.result.append([''.join(row) for row in self.board])
            return
        # Duyệt qua từng cột
        for col in range(n):
            # Kiểm tra xem có thể đặt một con hậu tại vị trí này hay không
            if self.isSafe(row, col, n):
                # Đặt hậu vào vị trí này
                self.board[row][col] = 'Q'
                # Gọi đệ quy để xử lý hàng tiếp theo
                self.solve(row + 1, n)
                # Quay lui và thử các vị trí khác
                self.board[row][col] = '.'
                
    def isSafe(self, row, col, n):
        # Kiểm tra hàng ngang
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        # Kiểm tra đường chéo chính (trái trên)
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if self.board[i][j] == 'Q':
                return False
        # Kiểm tra đường chéo phụ (phải trên)
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if self.board[i][j] == 'Q':
                return False
        return True
