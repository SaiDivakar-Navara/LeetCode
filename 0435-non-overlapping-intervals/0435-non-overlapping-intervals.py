class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        prev = intervals[0][1]
        count = 0
        for i in range(1, n):
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
            else:
                count += 1
        return count