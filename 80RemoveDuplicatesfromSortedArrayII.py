class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kiểm tra nếu mảng rỗng
        if not nums:
            return 0
        
        # Con trỏ hiện tại và con trỏ cho vị trí phần tử tiếp theo được ghi đè
        current, next_position = 0, 1
        
        # Số lần xuất hiện của phần tử hiện tại
        count = 1
        
        # Duyệt qua mảng nums
        while next_position < len(nums):
            # Nếu phần tử tiếp theo giống với phần tử hiện tại
            if nums[next_position] == nums[current]:
                # Nếu phần tử hiện tại đã xuất hiện 2 lần
                if count == 2:
                    next_position += 1
                else:
                    # Copy phần tử tiếp theo vào vị trí tiếp theo của phần tử hiện tại
                    current += 1
                    nums[current] = nums[next_position]
                    next_position += 1
                    count += 1
            else:
                # Nếu phần tử tiếp theo khác với phần tử hiện tại
                # Di chuyển con trỏ và đặt số lần xuất hiện của phần tử hiện tại về 1
                current += 1
                nums[current] = nums[next_position]
                next_position += 1
                count = 1
        
        # Trả về độ dài của mảng sau khi loại bỏ các phần tử trùng lặp
        return current + 1
