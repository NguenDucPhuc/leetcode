class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Tạo một từ điển để lưu trữ giá trị và chỉ số của các phần tử đã xét
        seen = {}
        
        # Duyệt qua từng phần tử trong mảng nums
        for i, num in enumerate(nums):
            # Tính toán giá trị cần tìm để đạt được target
            complement = target - num
            
            # Kiểm tra xem giá trị cần tìm đã xuất hiện trong từ điển chưa
            if complement in seen:
                # Nếu đã xuất hiện, trả về chỉ số của cặp số thỏa mãn
                return [seen[complement], i]
            else:
                # Nếu chưa, lưu lại giá trị và chỉ số của số hiện tại vào từ điển
                seen[num] = i
""
        