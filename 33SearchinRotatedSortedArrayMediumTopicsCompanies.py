class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Nếu phần tử ở vị trí mid lớn hơn hoặc bằng phần tử đầu tiên của mảng và phần tử target nằm trong khoảng giữa đầu mảng và mid
            if nums[mid] >= nums[left] and nums[left] <= target < nums[mid]:
                right = mid - 1
            # Nếu phần tử ở vị trí mid nhỏ hơn hoặc bằng phần tử cuối cùng của mảng và phần tử target nằm trong khoảng giữa mid và cuối mảng
            elif nums[mid] <= nums[right] and nums[mid] < target <= nums[right]:
                left = mid + 1
            # Nếu phần tử ở vị trí mid nhỏ hơn phần tử đầu tiên của mảng
            elif nums[mid] < nums[left]:
                right = mid - 1
            # Trường hợp còn lại: phần tử ở vị trí mid lớn hơn phần tử cuối cùng của mảng
            else:
                left = mid + 1
        
        return -1