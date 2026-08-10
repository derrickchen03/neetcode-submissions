class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        result = []

        def dfs(x, y, prevHeight, s):
            if x < 0 or y < 0 or x >= rows or y >= cols or (x, y) in s or heights[x][y] < prevHeight:
                return
            
            s.add((x, y))
            dfs(x + 1, y, heights[x][y], s)
            dfs(x - 1, y, heights[x][y], s)
            dfs(x, y + 1, heights[x][y], s)
            dfs(x, y - 1, heights[x][y], s)
        
        for x in range(rows):
            for y in range(cols):
                if x == 0 or y == 0:
                    dfs(x, y, heights[x][y], pacific)
                if x == rows - 1 or y == cols - 1:
                    dfs(x, y, heights[x][y], atlantic)
        
        for i in pacific:
            if i in atlantic:
                result.append([i[0], i[1]])
        return result