"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = sorted(i.start for i in intervals)
        e = sorted(i.end for i in intervals)

        s_p, e_p, count, r  = 0, 0, 0, 0

        while s_p < len(intervals):
            if s[s_p] < e[e_p]:
                s_p += 1
                count += 1
            else:
                count -= 1
                e_p += 1
        
            r = max(count, r)

        return r



        