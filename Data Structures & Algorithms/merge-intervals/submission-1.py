class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in intervals:
            if res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][0] = min(res[-1][0], i[0])
                res[-1][1] = max(res[-1][1], i[1])
        return res