class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # Xử lý trường hợp giống nhau
            while left < mid and nums[left] == nums[mid]:
                left += 1
                
            # Kiểm tra phần nằm trong khoảng
            if nums[left] <= nums[mid]:
                # Kiểm tra target có nằm trong phần nằm bên trái không
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Kiểm tra target có nằm trong phần nằm bên phải không
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
