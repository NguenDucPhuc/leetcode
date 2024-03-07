class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        k = 0  # Khởi tạo số lượng các phần tử không phải là mục tiêu
        
        # Duyệt qua mảng
        for i in range(len(nums)):
            # Nếu phần tử hiện tại không bằng giá trị mục tiêu
            if nums[i] != val:
                # Cập nhật phần tử hiện tại vào vị trí của k
                nums[k] = nums[i]
                # Tăng số lượng các phần tử không phải là mục tiêu
                k += 1
        
        return k