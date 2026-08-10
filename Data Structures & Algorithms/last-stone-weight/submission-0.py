import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in stones:
            heapq.heappush_max(h, i)
        while len(h) > 1:
            x = heapq.heappop_max(h)
            y = heapq.heappop_max(h)
            if x == y:
                continue
            else:
                heapq.heappush_max(h, (max(x,y) - min(x,y)))
        if h:
            return h[0]
        return 0