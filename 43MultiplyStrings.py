class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                total = mul + result[i + j + 1]
                result[i + j] += total // 10
                result[i + j + 1] = total % 10
        
        # Bỏ qua các số 0 không cần thiết ở đầu kết quả
        idx = 0
        while idx < len(result) and result[idx] == 0:
            idx += 1
        
        return ''.join(map(str, result[idx:]))
