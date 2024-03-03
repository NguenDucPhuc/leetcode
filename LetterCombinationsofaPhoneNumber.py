class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Xây dựng một bảng chữ cái tương ứng với các số từ 2 đến 9
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        # Hàm backtrack để tạo các kết hợp
        def backtrack(combination, next_digits):
            # Nếu không còn chữ số nào trong next_digits
            if len(next_digits) == 0:
                # Thêm kết hợp hiện tại vào danh sách kết quả
                output.append(combination)
            else:
                # Duyệt qua từng ký tự tương ứng với chữ số đầu tiên trong next_digits
                for letter in phone[next_digits[0]]:
                    # Gọi đệ quy backtrack với kết hợp hiện tại cộng với ký tự hiện tại và next_digits bỏ đi ký tự đầu tiên
                    backtrack(combination + letter, next_digits[1:])
        
        output = []
        if digits:
            backtrack("", digits)
        return output

# Sử dụng:
solution = Solution()
digits1 = "23"
print(solution.letterCombinations(digits1))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

digits2 = ""
print(solution.letterCombinations(digits2))  # Output: []

digits3 = "2"
print(solution.letterCombinations(digits3))  # Output: ["a","b","c"]
