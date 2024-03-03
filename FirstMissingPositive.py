class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Đánh dấu các số không thỏa mãn yêu cầu
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        # Tìm số nhỏ nhất bị thiếu
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Trường hợp mảng nums chứa tất cả các số từ 1 đến n
        return n + 1
