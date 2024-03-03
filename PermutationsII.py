class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(curr_permutation):
            # Nếu hoán vị hiện tại có độ dài bằng với độ dài của nums, thêm nó vào danh sách kết quả
            if len(curr_permutation) == len(nums):
                permutations.append(curr_permutation[:])
                return
            
            # Duyệt qua từng số trong nums
            for i in range(len(nums)):
                # Kiểm tra nếu số đã được sử dụng trong hoán vị hiện tại hoặc đã được sử dụng trước đó
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                # Đánh dấu số đã được sử dụng và thêm nó vào hoán vị hiện tại
                visited[i] = True
                curr_permutation.append(nums[i])
                # Tiếp tục đệ quy với hoán vị mới
                backtrack(curr_permutation)
                # Trả lại trạng thái ban đầu trước khi thêm số vào hoán vị
                visited[i] = False
                curr_permutation.pop()
        
        # Sắp xếp mảng nums để nhóm các số trùng lặp
        nums.sort()
        # Khởi tạo danh sách kết quả và danh sách đánh dấu cho việc sử dụng các số trong nums
        permutations = []
        visited = [False] * len(nums)
        backtrack([])
        return permutations
