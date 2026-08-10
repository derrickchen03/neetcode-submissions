import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        total = 0

        h = [(0, 0)]

        while h and len(visited) < n:
            weight, curr = heapq.heappop(h)

            if curr in visited:
                continue

            visited.add(curr)
            total += weight

            x1, y1 = points[curr]
            for next_node in range(n):
                if next_node not in visited:
                    x2, y2 = points[next_node]
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(h, (distance, next_node))
        return total