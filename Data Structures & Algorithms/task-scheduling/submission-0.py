from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        q = deque()
        d = {}
        r = []
        t = 0
        for i in tasks:
            d[i] = d.get(i, 0) + 1
        
        for i in d:
            heapq.heappush_max(h ,(d[i], i))
        
        while h or q:
            if q and t == q[0][2]:
                a = q.popleft()
                heapq.heappush_max(h, (a[1], a[0]))
            if h:
                x = heapq.heappop_max(h)
                if x[0] > 1:
                    q.append((x[1], x[0] - 1, t + n + 1))
                r.append(x[1])
            else:
                r.append("idle")
            t += 1
        return len(r)