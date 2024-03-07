class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Sắp xếp các interval theo giá trị bắt đầu
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_merged_interval = merged[-1]

            # Kiểm tra nếu interval hiện tại giao nhau với interval cuối cùng đã hợp nhất
            if current_interval[0] <= last_merged_interval[1]:
                # Hợp nhất các interval
                last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
            else:
                # Nếu không giao nhau, thêm interval hiện tại vào danh sách đã hợp nhất
                merged.append(current_interval)

        return merged
