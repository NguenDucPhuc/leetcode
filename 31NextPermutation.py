class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Tìm phần tử đầu tiên giảm dần từ phải sang trái
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Nếu tồn tại phần tử như vậy, tìm phần tử nhỏ nhất lớn hơn nums[i] từ phải sang trái
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Hoán đổi nums[i] và nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Đảo ngược các phần tử từ i+1 đến cuối danh sách
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1