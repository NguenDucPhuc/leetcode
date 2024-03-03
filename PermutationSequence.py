import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Khởi tạo danh sách chứa các số từ 1 đến n
        nums = [str(i) for i in range(1, n + 1)]
        # Khởi tạo chuỗi kết quả
        result = ''
        # Tính chỉ số bắt đầu từ 0
        k -= 1
        
        # Duyệt qua từng chữ số trong dãy số từ 1 đến n
        for i in range(n):
            # Tính chỉ số của chữ số tiếp theo trong dãy
            index = k // math.factorial(n - i - 1)
            # Thêm chữ số vào chuỗi kết quả
            result += nums[index]
            # Loại bỏ chữ số đã được thêm vào chuỗi kết quả
            nums.pop(index)
            # Cập nhật giá trị của k
            k %= math.factorial(n - i - 1)
        
        return result
