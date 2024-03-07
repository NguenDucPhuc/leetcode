class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Xử lý trường hợp cơ bản
        if n == 0:
            return 1
        
        # Xử lý trường hợp mũ âm
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:
            # Nếu mũ là số lẻ, nhân thêm một lần nữa với x
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2  # Chia mũ cho 2 để tiếp tục lặp
        return result
