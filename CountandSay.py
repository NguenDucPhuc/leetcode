class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        prev_str = self.countAndSay(n - 1)
        result = ""
        
        count = 1
        for i in range(len(prev_str)):
            if i < len(prev_str) - 1 and prev_str[i] == prev_str[i + 1]:
                count += 1
            else:
                result += str(count) + prev_str[i]
                count = 1
                
        return result
