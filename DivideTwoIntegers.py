class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Trường hợp đặc biệt: nếu divisor là 0 hoặc dividend là giá trị tối thiểu và divisor là -1
        if divisor == 0 or (dividend == -2147483648 and divisor == -1):
            return 2147483647
        
        # Xác định dấu của kết quả
        sign = (dividend > 0) ^ (divisor > 0)
        
        # Chuyển cả dividend và divisor thành các số dương
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        # Khởi tạo kết quả
        quotient = 0
        
        # Lặp cho đến khi dividend lớn hơn hoặc bằng divisor
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            
            # Tìm bội của divisor gần với dividend nhất
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            # Trừ bội của divisor từ dividend và cập nhật kết quả
            dividend -= temp_divisor
            quotient += multiple
        
        # Áp dụng dấu vào kết quả
        if sign:
            return -quotient
        else:
            return quotient