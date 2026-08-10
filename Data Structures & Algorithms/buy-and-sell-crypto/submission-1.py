class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        for i in range(len(prices) - 1):
            store = max(prices[i + 1:]) - prices[i]
            if curr_max < store:
                curr_max = store

        return curr_max