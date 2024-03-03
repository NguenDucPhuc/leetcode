class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Sử dụng phương pháp backtracking để đếm số lượng cách sắp xếp n-queens
        self.count = 0
        self.solve(0, n, [])
        return self.count
    
    def solve(self, row, n, queens):
        # Nếu đã xử lý hết tất cả các hàng, tăng biến đếm lên 1
        if row == n:
            self.count += 1
            return
        # Duyệt qua từng cột trong hàng hiện tại
        for col in range(n):
            # Kiểm tra xem có thể đặt một con hậu tại vị trí này hay không
            if self.isSafe(row, col, queens):
                # Nếu có thể đặt, thêm vị trí này vào danh sách queens
                queens.append(col)
                # Gọi đệ quy để xử lý hàng tiếp theo
                self.solve(row + 1, n, queens)
                # Quay lui và thử các vị trí khác
                queens.pop()
                
    def isSafe(self, row, col, queens):
        # Kiểm tra xem vị trí này có an toàn không
        for i, queen_col in enumerate(queens):
            # Kiểm tra xem có cùng một cột hoặc đường chéo với các con hậu trước đó không
            if queen_col == col or abs(row - i) == abs(col - queen_col):
                return False
        return True
