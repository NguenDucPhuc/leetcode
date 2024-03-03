class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Sắp xếp mảng đầu vào để dễ dàng thao tác
        nums.sort()
        n = len(nums)
        res = []
        
        # Duyệt qua từng cặp số duy nhất
        for i in range(n - 3):
            # Loại bỏ trường hợp trùng lặp
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Giảm bài toán 4Sum về bài toán 3Sum
            for j in range(i + 1, n - 2):
                # Loại bỏ trường hợp trùng lặp
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Sử dụng hai con trỏ để tìm kiếm cặp số thích hợp
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Loại bỏ trường hợp trùng lặp
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Di chuyển con trỏ
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return res

# Sử dụng:
solution = Solution()
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
print(solution.fourSum(nums1, target1))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

nums2 = [2, 2, 2, 2, 2]
target2 = 8
print(solution.fourSum(nums2, target2))  # Output: [[2, 2, 2, 2]]
