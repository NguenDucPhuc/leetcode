class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Thực hiện hoán đổi hàng và cột của ma trận
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Xoay từng hàng của ma trận
        for i in range(n):
            matrix[i] = matrix[i][::-1]
