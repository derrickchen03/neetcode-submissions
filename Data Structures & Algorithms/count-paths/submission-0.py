class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            dp[row][0] = 1 
        for col in range(n):
            dp[0][col] = 1 
    
        for i in range(m):
            if i == 0:
                continue

            for j in range(n):
                if j == 0:
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
        return dp[m - 1][n - 1]