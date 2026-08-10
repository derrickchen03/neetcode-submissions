class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s = [0] * (len(cost))
        s[0] = cost[0]
        s[1] = cost[1]

        for i in range(2, len(cost)):
            s[i] = cost[i] + min(s[i - 1], s[i - 2])
        return(min(s[-1], s[-2]))
