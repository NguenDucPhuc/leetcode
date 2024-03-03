class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sắp xếp mảng
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        result = 0
        
        # Duyệt qua mỗi phần tử
        for i in range(n - 2):
            # Thiết lập con trỏ left và right
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Tính khoảng cách giữa tổng và target
                diff = abs(total - target)
                
                # Cập nhật min_diff nếu cần
                if diff < min_diff:
                    min_diff = diff
                    result = total
                
                # Nếu tổng nhỏ hơn target, di chuyển left về phía bên phải
                if total < target:
                    left += 1
                # Nếu tổng lớn hơn target, di chuyển right về phía bên trái
                elif total > target:
                    right -= 1
                # Nếu tổng bằng target, trả về kết quả ngay lập tức
                else:
                    return total
        
        return result

# Sử dụng:
solution = Solution()
nums1 = [-1, 2, 1, -4]
target1 = 1
print(solution.threeSumClosest(nums1, target1))  # Output: 2

nums2 = [0, 0, 0]
target2 = 1
print(solution.threeSumClosest(nums2, target2))  # Output: 0
