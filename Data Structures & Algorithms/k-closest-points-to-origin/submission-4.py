import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt( ((0 - x) ** 2) + ((0 - y) ** 2))
        h = []
        r = []
        for i in points:
            v = dist(i[0], i[1])
            if len(h) < k:
                heapq.heappush_max(h, (v, i))
            else:
                if v < dist(h[0][1][0], h[0][1][1]):
                    heapq.heappop_max(h)
                    heapq.heappush_max(h, (v, i))
        for z in h:
            r.append(z[1])
        return r

        