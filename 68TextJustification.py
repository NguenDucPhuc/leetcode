class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = []
        line_length = 0
        
        for word in words:
            # Nếu thêm từ vào dòng hiện tại không vượt quá maxWidth
            if line_length + len(word) + len(line) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                # Tạo dòng mới từ các từ trong dòng hiện tại
                result.append(self.create_line(line, maxWidth))
                # Reset dòng mới với từ hiện tại
                line = [word]
                line_length = len(word)
        
        # Xử lý dòng cuối cùng
        result.append(" ".join(line).ljust(maxWidth))
        
        return result
    
    def create_line(self, line, maxWidth):
        # Nếu chỉ có một từ trong dòng
        if len(line) == 1:
            return line[0].ljust(maxWidth)
        
        # Tính số lượng khoảng trắng cần thêm vào mỗi từ
        total_spaces = maxWidth - sum(len(word) for word in line)
        spaces_between_words, extra_spaces = divmod(total_spaces, len(line) - 1)
        
        # Tạo dòng từ các từ trong dòng
        justified_line = ""
        for i in range(len(line) - 1):
            justified_line += line[i] + " " * spaces_between_words
            # Thêm extra space vào từng từ ở bên trái
            if i < extra_spaces:
                justified_line += " "
        # Thêm từ cuối cùng vào dòng
        justified_line += line[-1]
        
        return justified_line
        