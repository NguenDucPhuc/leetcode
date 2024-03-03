from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Khởi tạo một từ điển để lưu trữ các nhóm anagram
        anagrams = defaultdict(list)
        
        # Lặp qua từng chuỗi trong danh sách strs
        for s in strs:
            # Sắp xếp các ký tự trong chuỗi để tạo ra một khóa đại diện
            # Các chuỗi có cùng một khóa sẽ được coi là các anagram của nhau
            key = ''.join(sorted(s))
            # Thêm chuỗi vào danh sách tương ứng với khóa trong từ điển
            anagrams[key].append(s)
        
        # Trả về danh sách các nhóm anagram
        return list(anagrams.values())
