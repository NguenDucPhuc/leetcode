class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(curr_permutation):
            # Nếu hoán vị hiện tại đã có độ dài bằng với độ dài của nums, thêm hoán vị đó vào danh sách kết quả
            if len(curr_permutation) == len(nums):
                permutations.append(curr_permutation[:])
                return
            
            # Duyệt qua từng số trong nums
            for num in nums:
                # Nếu số đã được thêm vào hoán vị hiện tại, bỏ qua
                if num in curr_permutation:
                    continue
                # Thêm số vào hoán vị hiện tại và tiếp tục đệ quy
                curr_permutation.append(num)
                backtrack(curr_permutation)
                # Loại bỏ số vừa thêm vào hoán vị để thử với số khác trong lần đệ quy tiếp theo
                curr_permutation.pop()
        
        # Khởi tạo danh sách kết quả và gọi hàm backtrack để tạo các hoán vị
        permutations = []
        backtrack([])
        return permutations
