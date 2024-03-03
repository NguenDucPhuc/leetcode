class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Khởi tạo ma trận nxn với tất cả các phần tử bằng 0
        matrix = [[0] * n for _ in range(n)]
        # Định nghĩa các biến để xác định hướng di chuyển
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        direction_index = 0
        # Khởi tạo giới hạn trên, dưới, trái, phải
        top, bottom, left, right = 0, n - 1, 0, n - 1
        # Khởi tạo biến để lưu giá trị của mỗi ô
        num = 1
        
        # Bắt đầu đi theo chiều xoắn ốc và gán giá trị cho mỗi ô
        while num <= n * n:
            if direction_index == 0:  # right
                for i in range(left, right + 1):
                    matrix[top][i] = num
                    num += 1
                top += 1
            elif direction_index == 1:  # down
                for i in range(top, bottom + 1):
                    matrix[i][right] = num
                    num += 1
                right -= 1
            elif direction_index == 2:  # left
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            elif direction_index == 3:  # up
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
            # Cập nhật hướng di chuyển
            direction_index = (direction_index + 1) % 4
        
        return matrix
