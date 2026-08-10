from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        while q:
            row, col = q.popleft()

            for r,c in directions:
                newr = row + r
                newc = col + c

                if (newr < 0 or newc < 0 or newr >= len(grid) or newc >= len(grid[0]) or grid[newr][newc] != 2147483647):
                    continue
                
                grid[newr][newc] = grid[row][col] + 1
                q.append((newr, newc))
