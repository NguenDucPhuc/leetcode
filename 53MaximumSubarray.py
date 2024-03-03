class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]  # tổng lớn nhất là phần tử đầu tiên
        current_sum = nums[0]  # hiện tại là phần tử đầu tiên
        
        # Duyệt qua từng phần tử của mảng, từ phần tử thứ hai
        for num in nums[1:]:
            # Cập nhật tổng hiện tại bằng tổng của tổng hiện tại và phần tử hiện tại hoặc chỉ phần tử hiện tại
            current_sum = max(num, current_sum + num)
            # Cập nhật tổng lớn nhất
            max_sum = max(max_sum, current_sum)
        
        return max_sum
