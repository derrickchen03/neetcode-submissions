class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        r = 0
        prev = intervals[0][1]

        for i in intervals[1:]:
            if prev <= i[0]:
                prev = i[1]
                continue
            else:
                prev = min(prev, i[1])
                r += 1
        return r