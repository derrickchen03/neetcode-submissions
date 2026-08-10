import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dist = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dist[0][0] = grid[0][0]

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = [(grid[0][0], 0, 0)]

        while q:
            h, r, c = heapq.heappop(q)

            if h > dist[r][c]:
                continue
            
            for dr, dc in dir:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue

                new_h = max(h, grid[nr][nc])

                if new_h < dist[nr][nc]:
                    dist[nr][nc] = new_h
                    heapq.heappush(q, (new_h, nr, nc))

        return dist[len(grid)-1][len(grid[0])-1]

        