class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        result = []
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        while top <= bottom and left <= right:
            # Duyệt hàng đầu tiên từ trái qua phải
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Duyệt cột cuối cùng từ trên xuống dưới
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Kiểm tra xem có hàng dưới còn không
            if top <= bottom:
                # Duyệt hàng cuối cùng từ phải qua trái
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # Kiểm tra xem có cột bên trái còn không
            if left <= right:
                # Duyệt cột đầu tiên từ dưới lên trên
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result
