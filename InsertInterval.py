class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        i = 0
        n = len(intervals)

        # Thêm tất cả các interval có start < newInterval[0] vào danh sách hợp nhất
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Hợp nhất các interval giao nhau với newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Thêm interval đã hợp nhất vào danh sách hợp nhất
        merged.append(newInterval)

        # Thêm tất cả các interval còn lại vào danh sách hợp nhất
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged
