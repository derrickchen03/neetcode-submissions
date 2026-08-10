class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(1, len(s)):
            single = s[i]
            double = s[i - 1 : i + 1]

            if single != "0":
                dp[i + 1] += dp[i]
            
            if 10 <= int(double) <= 26:
                dp[i + 1] += dp[i - 1]
        
        return dp[len(s)]