class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])  # Độ dài của mỗi từ trong words
        total_len = len(words) * word_len  # Tổng độ dài của tất cả các từ trong words
        
        word_count = {}  # Tạo một từ điển để lưu số lần xuất hiện của mỗi từ trong words
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []  # Danh sách để lưu kết quả cuối cùng
        
        # Duyệt qua từng vị trí bắt đầu trong chuỗi s
        for i in range(len(s) - total_len + 1):
            # Tạo một từ điển để lưu số lần xuất hiện của mỗi từ trong từng chuỗi con có độ dài total_len
            temp_count = {}
            
            # Duyệt qua từng từ trong từng chuỗi con có độ dài total_len
            for j in range(i, i + total_len, word_len):
                word = s[j:j + word_len]
                temp_count[word] = temp_count.get(word, 0) + 1
            
            # So sánh từ điển temp_count với từ điển word_count
            if temp_count == word_count:
                result.append(i)
        
        return result