class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()  # Bỏ khoảng trắng ở đầu và cuối chuỗi
        if not s:
            return False
        
        has_digit = False
        has_dot = False
        has_e = False
        has_sign = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                has_digit = True
            elif char in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
                has_sign = True
            elif char == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif char in ['e', 'E']:
                if not has_digit or has_e:
                    return False
                has_e = True
                has_digit = False
            else:
                return False
        
        return has_digit
