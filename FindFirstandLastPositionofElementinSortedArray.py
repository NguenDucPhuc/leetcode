class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(nums) and nums[left] == target else -1

        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right if right >= 0 and nums[right] == target else -1

        left = binarySearchLeft(nums, target)
        if left == -1:
            return [-1, -1]
        right = binarySearchRight(nums, target)
        return [left, right]

# Sử dụng
solution = Solution()
nums1 = [5,7,7,8,8,10]
target1 = 8
print(solution.searchRange(nums1, target1))  # Output: [3, 4]

nums2 = [5,7,7,8,8,10]
target2 = 6
print(solution.searchRange(nums2, target2))  # Output: [-1, -1]

nums3 = []
target3 = 0
print(solution.searchRange(nums3, target3))  # Output: [-1, -1]
