class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Hàm kiểm tra tính hợp lệ của giá trị được đặt vào ô cụ thể
        def isValid(row, col, num):
            for i in range(9):
                if board[i][col] == num or board[row][i] == num or \
                   board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True
        
        # Hàm đệ quy để giải Sudoku
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if isValid(i, j, num):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True
        
        solve()
        
# Sử dụng
solution = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution.solveSudoku(board)
print(board)
