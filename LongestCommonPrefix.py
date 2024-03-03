class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Lặp qua từng ký tự từ đầu đến khi không còn ký tự nào hoặc không giống nhau
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]  # Trường hợp tất cả các chuỗi giống nhau

# Sử dụng:
solution = Solution()
strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs2))  # Output: ""
