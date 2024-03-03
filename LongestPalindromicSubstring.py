class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Hàm mở rộng từ một vị trí để tìm chuỗi con palindromic
        def expand_around_center(left, right):
            # Mở rộng từ vị trí left và right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Trả về chuỗi con palindromic
            return s[left+1:right]

        # Biến lưu trữ chuỗi con palindromic dài nhất
        longest = ""

        # Duyệt qua từng vị trí trong chuỗi
        for i in range(len(s)):
            # Trường hợp chuỗi palindromic có độ dài lẻ
            palindrome_odd = expand_around_center(i, i)
            # Trường hợp chuỗi palindromic có độ dài chẵn
            palindrome_even = expand_around_center(i, i + 1)
            # Chọn chuỗi palindromic dài nhất từ hai trường hợp trên
            current_longest = palindrome_odd if len(palindrome_odd) > len(palindrome_even) else palindrome_even
            # So sánh với chuỗi palindromic dài nhất đã biết
            if len(current_longest) > len(longest):
                longest = current_longest

        return longest
