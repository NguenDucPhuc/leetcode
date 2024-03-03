class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0:
            # Lấy các chữ số hiện tại từ a và b (hoặc 0 nếu đã duyệt hết)
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Cộng các chữ số cùng với phần nhớ
            total = digit_a + digit_b + carry
            
            # Cập nhật phần nhớ và tính tổng chữ số
            carry = total // 2
            digit_sum = total % 2
            
            # Thêm chữ số tổng vào kết quả
            result = str(digit_sum) + result
            
            # Di chuyển đến các chữ số tiếp theo
            i -= 1
            j -= 1
        
        # Nếu vẫn còn phần nhớ, thêm vào kết quả
        if carry:
            result = "1" + result
        
        return result