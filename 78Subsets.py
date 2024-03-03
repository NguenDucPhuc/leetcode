class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, subset):
            # Thêm tập con hiện tại vào danh sách kết quả
            result.append(subset[:])
            
            # Duyệt qua các phần tử từ start đến hết mảng nums
            for i in range(start, len(nums)):
                # Thêm phần tử hiện tại vào tập con
                subset.append(nums[i])
                # Duyệt tiếp tục với phần tử tiếp theo
                backtrack(i + 1, subset)
                # Sau khi duyệt xong một nhánh, loại bỏ phần tử hiện tại để thử các phần tử khác
                subset.pop()
        
        result = []
        backtrack(0, [])
        return result
