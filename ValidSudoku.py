class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Kiểm tra tính hợp lệ của từng hàng
        for row in board:
            if not self.isValidUnit(row):
                return False
        
        # Kiểm tra tính hợp lệ của từng cột
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        
        # Kiểm tra tính hợp lệ của từng 3x3 sub-box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValidUnit(sub_box):
                    return False
        
        return True
    
    def isValidUnit(self, unit):
        seen = set()
        for digit in unit:
            if digit != '.':
                if digit in seen:
                    return False
                seen.add(digit)
        return True

# Sử dụng
solution = Solution()
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board1))  # Output: True

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board2))  # Output: False
