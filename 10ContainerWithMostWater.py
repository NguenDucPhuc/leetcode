class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            # Tính diện tích của hình chữ nhật được tạo bởi hai đường cao hơn
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            # Di chuyển con trỏ tại đầu và cuối mảng
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
