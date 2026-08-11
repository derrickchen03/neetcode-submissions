from collections import defaultdict

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)

        def rec(i, holding):
            if i >= len(prices):
                return 0
            
            if (i, holding) in dp:
                return dp[(i, holding)]

            if holding:
                dp[(i, holding)] = max(rec(i + 2, False) + prices[i], rec(i + 1, True))
                
            else:
                dp[(i, holding)] = max(rec(i + 1, True) - prices[i], rec(i + 1, False))
            
            return dp[(i, holding)]
        
        return rec(0, False)
            
            