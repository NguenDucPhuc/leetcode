class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        
        # Khởi tạo các biến
        jumps = 0 # Số lần nhảy cần thiết
        farthest = 0 # Biến lưu trữ chỉ số xa nhất có thể đạt được từ vị trí hiện tại
        end = 0 # Biến lưu trữ chỉ số cuối cùng trong mỗi bước nhảy
        
        # Duyệt qua từng vị trí trong nums
        for i in range(n - 1):
            # Tìm chỉ số xa nhất có thể đạt được từ vị trí hiện tại
            farthest = max(farthest, i + nums[i])
            
            # Nếu đã đạt được cuối cùng trong phạm vi hiện tại, cập nhật cuối cùng và tăng số lần nhảy
            if i == end:
                end = farthest
                jumps += 1
        
        return jumps
