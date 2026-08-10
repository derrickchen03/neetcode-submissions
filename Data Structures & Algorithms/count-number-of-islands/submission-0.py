class Solution:
        def numIslands(self, grid: List[List[str]]) -> int:
            visited = [
                [False for _ in range(len(grid[0]))]
                for _ in range(len(grid))
            ]

            res = 0

            def findIsland(x, y):
                if (
                    x < 0
                    or y < 0
                    or x >= len(grid)
                    or y >= len(grid[0])
                    or grid[x][y] == "0"
                    or visited[x][y]
                ):
                    return

                visited[x][y] = True

                findIsland(x + 1, y)
                findIsland(x - 1, y)
                findIsland(x, y + 1)
                findIsland(x, y - 1)

            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == "1" and not visited[row][col]:
                        findIsland(row, col)
                        res += 1

            return res