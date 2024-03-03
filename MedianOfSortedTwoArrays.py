class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Kết hợp hai mảng thành một mảng được sắp xếp
        merged = sorted(nums1 + nums2)
        n = len(merged)

        # Tìm trung vị của mảng đã kết hợp
        if n % 2 == 0:
            # Nếu số lượng phần tử là chẵn, trung vị là trung bình của hai giá trị giữa
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        else:
            # Nếu số lượng phần tử là lẻ, trung vị là giá trị ở giữa
            return merged[n // 2]
