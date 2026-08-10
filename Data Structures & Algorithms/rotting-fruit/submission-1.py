from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            level = len(q)

            for x in range(level):
                y, z = q.popleft()

                for r, c in directions:
                    newr = y + r
                    newc = z + c
                    if (newr < 0 or newc < 0 or newr >= len(grid) or newc >= len(grid[0]) or grid[newr][newc] != 1):
                        continue
                    else:
                        grid[newr][newc] = 2
                        q.append((newr, newc))
            minutes += 1
        
        for i in grid:
            if 1 in i:
                return -1
        return max(minutes, 0)
        
        
        