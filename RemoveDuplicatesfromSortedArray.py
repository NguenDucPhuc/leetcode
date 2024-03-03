class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # Khởi tạo số lượng các phần tử duy nhất
        
        # Duyệt qua mảng bắt đầu từ phần tử thứ hai
        for i in range(1, len(nums)):
            # Nếu phần tử hiện tại khác với phần tử trước đó
            if nums[i] != nums[i - 1]:
                # Cập nhật phần tử hiện tại vào vị trí của k
                nums[k] = nums[i]
                # Tăng số lượng các phần tử duy nhất
                k += 1
        
        return k
