class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row == len(matrix) or col == len(matrix[0]):
                return 0
        
            directions = [1, 0], [-1, 0], [0, 1], [0, -1]
            if (row, col) in visited:
                return dp[row][col]
            
            visited.add((row, col))
            
            for ni, nj in directions:
                nr = ni + row
                nc = nj + col
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                    if matrix[nr][nc] > matrix[row][col]:
                        dp[row][col] = max(dfs(nr, nc) + 1, dp[row][col])
            
            return dp[row][col]

        answer = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                answer = max(answer, dfs(i, j ))
        return answer
            
            

                