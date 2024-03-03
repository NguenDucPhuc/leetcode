class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sắp xếp mảng
        nums.sort()
        n = len(nums)
        result = []
        
        # Duyệt qua mỗi phần tử
        for i in range(n - 2):
            # Tránh trường hợp trùng lặp
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Thiết lập con trỏ left và right
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Tránh trường hợp trùng lặp
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

# Sử dụng:
solution = Solution()
nums1 = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print(solution.threeSum(nums2))  # Output: []

nums3 = [0, 0, 0]
print(solution.threeSum(nums3))  # Output: [[0, 0, 0]]
