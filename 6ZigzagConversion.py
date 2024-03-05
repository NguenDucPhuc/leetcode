class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Trường hợp đặc biệt
        if numRows == 1 or numRows >= len(s):
            return s

        # Khởi tạo một danh sách các chuỗi con cho mỗi hàng
        rows = [''] * numRows
        # Biến đếm cho hàng và hướng của biến đếm
        index, direction = 0, 1

        # Duyệt qua từng ký tự trong chuỗi
        for char in s:
            # Thêm ký tự vào chuỗi con của hàng hiện tại
            rows[index] += char
            # Nếu đang ở hàng đầu hoặc cuối, thay đổi hướng
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            # Tăng hoặc giảm chỉ số hàng tùy theo hướng
            index += direction

        # Kết hợp các chuỗi con của mỗi hàng để tạo ra chuỗi kết quả
        return ''.join(rows)
