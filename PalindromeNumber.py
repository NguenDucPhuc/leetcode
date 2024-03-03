class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Nếu số là số âm hoặc là số chia hết cho 10 nhưng không phải số 0, thì không phải palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Khởi tạo biến để lưu giá trị đảo của số
        reversed_num = 0

        # Lặp qua các chữ số của số ban đầu để tạo ra số đảo
        while x > reversed_num:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        # Kiểm tra xem số đảo có bằng số ban đầu không
        # Nếu số ban đầu có số chữ số lẻ, ta cần loại bỏ chữ số ở giữa của số đảo
        return x == reversed_num or x == reversed_num // 10
