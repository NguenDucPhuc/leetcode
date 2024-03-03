class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        # Duyệt qua chuỗi haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Kiểm tra xem chuỗi con hiện tại của haystack có khớp với needle không
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # Nếu không tìm thấy needle, trả về -1
        return -1